class NPV:

    def __init__(self,
                 parameters,
                 start_year,
                 start_month,
                 years,
                 cash_lag=3,
                 investment_months=[0],
                 investment_amounts=[0],
                 company_name=''):

        '''Creates the simulation model.

        model = npv.NPV()
        model.calculate('npv')

        parameters | dict or str | a text file or python dictionary with params
        start_year | int | the year when simulation starts
        start_month | int | the month when simulation starts
        years | int | number of years to simulate
        cash_lag | int | number of months it takes from delivery to cash in bank
        investment_months | list | months on which investment comes in
        investment_amounts | list | amounts of investment coming in
        company_name | str | the name of the company
        '''

        # load the parameters
        if isinstance(parameters, str):
            from .params import load_params_from_file
            self.params = load_params_from_file(parameters)
        else:
            self.params = parameters

        self._start_year = start_year
        self._start_month = start_month
        self._cash_lag = cash_lag
        self._investment_months = investment_months
        self._investment_amounts = investment_amounts

        self.company_name = company_name

        self.params['number_of_months'] = int(years * 12)

        _null = self.simulate_financials()

    def simulate_financials(self):

        import wrangle

        from .monthly_to_annual import monthly_to_annual
        from .monthly_cashflow import monthly_cashflow

        # build the monthly reports and growth stats
        self.monthly_income, self.monthly_stats = self._build_table()

        cols = wrangle.utils.create_time_sequence(self.params['number_of_months'],
                                                  self._start_year,
                                                  self._start_month)

        self.monthly_income.columns = cols
        self.monthly_stats.columns = cols

        # build annual reports and growth stats
        self.annual_income = monthly_to_annual(self.monthly_income)
        self.annual_stats = monthly_to_annual(self.monthly_stats)

        cols = list(range(self._start_year,
                          int(self.params['number_of_months'] / 12 + self._start_year),
                          1))

        self.annual_income.columns = cols
        self.annual_stats.columns = cols

        self.monthly_cashflow = monthly_cashflow(self.monthly_income,
                                                 self._cash_lag,
                                                 self._investment_months,
                                                 self._investment_amounts)

    def _build_table(self):

        '''Handles the main part of the simulation'''

        import copy
        import pandas as pd
        import numpy as np

        from .build_periods import build_periods
        from .salary_calculator import salary_calculator

        self._params = copy.deepcopy(self.params)

        # generate core data
        if self.params['core_static']:
            cores = np.full(self.params['number_of_months'], self.params['core'])
        else:
            cores = build_periods(self.params, 'core')

        # generate revenue data
        if self.params['revenue_static']:
            revenues = np.full(self.params['number_of_months'], self.params['revenue'])
        else:
            revenues = build_periods(self.params, 'revenue')

        # generate resource data
        if self.params['resource_static']:
            resources = np.full(self.params['number_of_months'], self.params['resource'])
        else:
            resources = build_periods(self.params, 'resource')

        # build annual revenue
        revenue = cores * revenues

        # build annual resource cost
        resource = cores * resources

        # build annual income tax
        tax = revenue * self.params['tax_rate']

        # build annual marketing cost
        marketing = revenue * self.params['marketing_cost']

        # build staff cost
        manpower_data = salary_calculator(self.params, cores)

        staff = manpower_data[0]
        headcount = manpower_data[1]

        # build COGS
        cogs = staff + resource

        # build gross profit
        gross_profit = revenue - cogs

        # other costs << note this needs a wildcard variable
        other_cost = marketing + (self.params['other_cost'] * cogs)

        # EBITDA
        ebitda = gross_profit - other_cost

        # EBIT
        # but first calculate depreciation_amortization
        depreciation_amortization = self.params['capital_investment'] / self.params['depreciation_years'] / 12
        ebit = ebitda - depreciation_amortization

        # NOPAT
        nopat = ebit - (ebit * self.params['tax_rate'])

        # OCFC
        ocfc = nopat + depreciation_amortization

        # depreciation and amortization
        depreciation_amortization = [depreciation_amortization] * len(cores)

        # move on to put everything together
        out = np.vstack([cores,
                         revenue,
                         resource,
                         tax,
                         marketing,
                         staff,
                         cogs,
                         gross_profit,
                         other_cost,
                         ebitda,
                         depreciation_amortization,
                         ebit,
                         nopat,
                         ocfc])

        out = pd.DataFrame(out)

        out.index = [
            'cores',
            'revenue',
            'resource',
            'tax',
            'marketing',
            'staff',
            'cogs',
            'gross_profit',
            'other_cost',
            'ebitda',
            'depreciation_amortization',
            'ebit',
            'nopat',
            'ocfc']

        out.columns = range(1, len(cores) + 1)

        headcount = pd.DataFrame(headcount).transpose()
        headcount.index = ['sales',
                           'production',
                           'manager',
                           'service',
                           'admin']

        self.params = copy.deepcopy(self._params)

        return out.astype(int), headcount

    def compute(self, mode='nvp', output='last'):

        '''Compute npv or other metrics based on financial data.

        mode | str | 'gross_profit', 'ebitda', 'ebit', 'nopat', 'ocfc'
        output | str | 'last', 'all', 'median', or 'mean'

        '''

        import numpy as np

        if mode == 'nvp':
            ocfc = self.annual_income.loc['ocfc'].values
            return int(np.npv(self.params['rate_of_return'], ocfc))

        else:

            results = self.annual_income.loc[mode].values

            if output == 'last':
                return results[-1]

            elif output == 'mean':
                return np.mean(results).tolist()

            elif output == 'median':
                return np.median(results).tolist()

            else:
                return results.tolist()

    def monte_carlo(self, n, mode='nvp'):

        '''Performns a Monte Carlo simulation for n rounds.

        mode | str | 'gross_profit', 'ebitda', 'ebit', 'nopat', 'ocfc'


        '''

        out = []

        for i in range(n):

            self.simulate_financials()
            out.append(self.compute(mode=mode, output='last'))

        return out
