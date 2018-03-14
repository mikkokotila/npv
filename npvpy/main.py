import numpy as np

class NPV:
    
    def __init__(self, parameters):
        
        if type(parameters) is str:
            self.p = self.load_params(parameters)
        else:
            self.p = parameters
            
    
    def load_params(self, filename):
        
        with open(filename, 'r') as f:
            s = f.read()
            out = ast.literal_eval(s)
        
        return out
    
    def _change_numbers(self, aspect_change, aspect_incertainty, aspect_steps):

        change_min = aspect_change - (aspect_change * aspect_incertainty)
        change_max = aspect_change + (aspect_change * aspect_incertainty)
        change_steps = (change_max - change_min) / aspect_steps
        change_outcomes = np.arange(change_min, change_max, change_steps)

        return change_outcomes
    
    def _pick_random(self, choices):
    
        return np.random.choice(choices)
    
    def _build_years(self, 
                     start_value,
                     change, 
                     incentainty,
                     steps,
                     number_of_years):
    
        annual_values = []

        change_outcomes = self._change_numbers(self.p[change],
                                               self.p[incentainty],
                                               self.p[steps])

        for i in range(self.p[number_of_years]):
            input_change = self._pick_random(change_outcomes)

            if i == 0:
                input_temp = self.p[start_value]

            else:
                input_temp = annual_values[i-1] + (input_change * annual_values[i-1])

            input_temp = int(input_temp)
            annual_values.append(input_temp)

        return np.array(annual_values)
    
    
    def _salary_calculator(self):

        staff_cost = []

        change_outcomes = self._change_numbers(self.p['salaries_change'],
                                               self.p['salaries_incertainty'], 
                                               self.p['salaries_steps'])

        for i in range(self.p['number_of_years']):

            # establishing individual values
            sales_total = self.p['sales_salary'] * (self.cores[i] / self.p['core_per_sales'])
            production_total = self.p['production_salary'] * (self.cores[i] / self.p['core_per_production'])
            manager_total = self.p['manager_salary'] * (self.cores[i] / self.p['core_per_manager'])
            service_total = self.p['service_salary'] * (self.cores[i] / self.p['core_per_service'])
            admin_total = self.p['admin_salary'] * (self.cores[i] / self.p['core_per_admin'])

            # summing up the individual values
            salaries_total = sales_total + production_total + manager_total + service_total + admin_total

            # getting the growth factor
            input_growth = self._pick_random(change_outcomes)

            if i == 0:
                staff_temp = salaries_total + (salaries_total * (self.p['employer_liabilities'] + self.p['employer_misc']))
            else:
                staff_temp = salaries_total + (salaries_total * (self.p['employer_liabilities'] + self.p['employer_misc']))
                staff_temp = staff_temp + (staff_temp * input_growth)

            staff_cost.append(int(staff_temp))

        return np.array(staff_cost)
    
    
    def _build_table(self):
        
        if self.p['core_static'] == True: 
            cores = np.full(self.p['number_of_years'],
                                 self.p['core'])
        else: 
            cores = self._build_years('core',
                                      'core_change',
                                      'core_incertainty',
                                      'core_steps',
                                      'number_of_years')
        self.cores = cores
            
        if self.p['core_static'] == True: 
            revenues = np.full(self.p['number_of_years'],
                               self.p['revenue'])
        else: 
            revenues = self._build_years('revenue',
                                         'revenue_change',
                                         'revenue_incertainty',
                                         'revenue_steps',
                                         'number_of_years')
            
        self.revenues = revenues
            
        if self.p['core_static'] == True: 
            resources = np.full(self.p['number_of_years'],
                                self.p['revenue'])
        else: 
            resources = self._build_years('resource',
                                          'resource_change',
                                          'resource_incertainty',
                                          'resource_steps',
                                          'number_of_years')
        
        self.resources = resources
        
        # build annual revenue 
        annual_revenue = cores * revenues

        # build annual resource cost
        annual_resource = cores * resources

        # build annual income tax 
        annual_tax = annual_revenue * self.p['tax_rate']

        # build annual marketing cost
        annual_marketing = annual_revenue * self.p['marketing_cost']
        
        # build staff cost
        annual_staff = self._salary_calculator()
        
        # build COGS
        cogs = annual_staff + annual_resource

        # build gross profit
        gross_profit = annual_revenue - cogs

        # other costs << note this needs a wildcard variable
        other_cost = annual_marketing 

        # EBITDA 
        ebitda = gross_profit - other_cost

        # EBIT
        # but first calculate depreciation_amortization
        depreciation_amortization = self.p['capital_investment'] / self.p['depreciation_years']
        ebit = ebitda - depreciation_amortization

        # NOPAT 
        nopat = ebit - (ebit * self.p['tax_rate'])

        # OCFC 
        ocfc = nopat + depreciation_amortization

        return ocfc
    
    def _calculate_npv(self):
        
        ocfc = self._build_table()
        npv = np.npv(self.p['rate_of_return'], ocfc)
        
        return npv
