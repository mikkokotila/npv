def monthly_cashflow(monthly_income,
                     cash_lag,
                     investment_months=[0],
                     investment_amounts=[0]):

    '''Computes Monthly Cashflow Statements

    monthly_income_statement | DataFrame | from NPV() instance
    cash_lag | int | number of months it takes from delivery to cash in bank
    investment_months | list | months on which investment comes in
    investment_amounts | list | amounts of investment coming in

    '''

    import pandas as pd

    periods = list(monthly_income.loc['revenue'])
    periods_len = len(periods)

    for i in range(cash_lag):
        periods.insert(0, 0)

    cash_in = periods[:periods_len]

    cash_out = monthly_income.loc['cogs'] + monthly_income.loc['marketing']

    d = pd.DataFrame({
        'cash_in': cash_in,
        'cash_out': cash_out,
    })

    stock_issuance = [0] * periods_len

    i = 0
    for period in investment_months:
        stock_issuance.pop(period)
        stock_issuance.insert(period, investment_amounts[i])
        i += 1

    d['stock_issuance'] = stock_issuance
    d['total_cash'] = d.cash_in.cumsum() + d.stock_issuance.cumsum() - d.cash_out.cumsum()

    d = d.transpose()

    return d
