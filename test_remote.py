from npv import NPV

model = NPV('params.txt', 2019, 8, 5)

model.annual_income
model.annual_stats
model.compute()
model.compute('ebitda')
model.compute('gross_profit')
model.monte_carlo(10, 'ebitda')
model.monthly_cashflow
model.monthly_income
model.monthly_stats
model.simulate_financials()
model.annual_income
model.annual_stats
model.compute()
model.compute('ebitda')
model.compute('gross_profit')
model.monte_carlo(10, 'ebitda')
model.monthly_cashflow
model.monthly_income
model.monthly_stats
model.simulate_financials()

model = NPV('params.txt',
            start_year=2021,
            start_month=1,
            years=10,
            cash_lag=8,
            investment_months=[1, 12, 18],
            investment_amounts=[100000, 500000, 1000000])
