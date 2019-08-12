![npvpy](https://raw.githubusercontent.com/mikkokotila/npvpy/master/logo.png)

# npv
Startup and Corporate Investment and Financial Planning Simulator for Python.

## 1. Overview

**NPV** provides a very high level simulation facility for getting the NPV (net presevent value) score for any business idea. By default, the simulation automatically generates:

- monthly and annual income statement
- monthly and annual cashflow statement
- monthly and annual growth statistics

Simulation is based on set of input variables and volatility computations that can be adjusted as needed for each project. 

Additionally, facility for performing a **Monte Carlo** simulation is provided, and a method for generating key financial metrics individually. 

### 1.1. About NPV

NPV, or Net Present Value, is the difference between the present value of cash inflows and the present value of cash outflows over a period of time. Its main use-case is in capital budgeting to analyze profitability of a projected investment or project[1].

NPV is widely used by managers and investors to support decision making on large investments. For long it has been the gold standard tool for merger and acquisition activity, but is referred to as the 'discounted cash flow model' in that context. In fact, NPV is the model that Warren Buffet uses to evaluate companies[2].


## 2. Install and Use

### 2.1 Install

`pip install npv`

or:

`pip install git+https://github.com/mikkokotila/npv.git`


### 2.2. Single Use

#### To import

`import npv`

#### Use with params in a dictionary

```
model = npv.NPV(params)
```

`model` now contains financial statements and other assets. 

#### Perform an Ebitda Monte Carlo simulation for 1,000 rounds

`model.monte_carlo(1000, 'ebitda')`

#### Use with params in a text file

```
model = npv.NPV('params.txt')
```

## 3. Parameters

### 3.1. Parameter Taxonomy

Parameter | Example Value | Description
-------|---------|---------
core | 100 | what the business is delivering
revenue | 30000 | revenue per delivery
resource | 8500 | cost of resource per delivery
core_change | 0.5 | maximum annual change of deliverable
core_incertainty | 1 | level of incertainty
core_steps | 30 | number choices between minimum and maximum
revenue_change | 0.2 | max annual change of revenue
revenue_incertainty | 1 | level of incertainty
revenue_steps | 100 | number choices between minimum and maximum
resource_change | 0.2 | max annual change of resouce cost
resource_incertainty | 0.2 | level of incertainty
resource_steps | 10 | number choices between minimum and maximum
sales_salary | 96000 | annual salary per sales person
production_salary | 75000 | annual salary per production person
manager_salary | 132000 |  annual salary per manager
service_salary | 96000 | annual salary per service person
admin_salary | 60000 | annual salary per admin person
core_per_sales | 10 | number deliverables a sales person can handle
core_per_production | 5 | number of deliverables a production person can handle
core_per_manager | 50 | number of deliverables a manager can handle
core_per_service | 20 | number of deliverables a service person can handle
core_per_admin | 200 | number of deliverables an admin person can handle
salaries_change | 0.05 | max annual change in sales
salaries_incertainty | 0.1 | level of incertainty
salaries_steps | 10 | number choices between minimum and maximum
employer_liabilities | 0.45 | extra costs in addition to salaries
employer_misc | 0.03 | other employer costs
marketing_cost | 0.1 | marketing cost as a factor of revenue
other_cost | 0.1 | other business costs
tax_rate | 0.21 | the tax rate the business is subject to
number_of_years | 10 | number of years to model
depreciation_years | 10 | how many years to depreciate investment
capital_investment | 100000 | initial investment into the business
rate_of_return | 0.1 | the rate of return (ROR)
risk_factor | 2 | a factor effects the likeliness of change to be negative
core_static | False | cores are same every year if True
revenue_static | False | revenue is same every year if True
resource_static | False | resource is same every year if True

Below some additional details is provided for (some of) the parameters.

#### FUNDAMENTAL PARAMETERS

There are three *fundamental aspects* in the model; the core deliverable, revenue per deliverable, and cost of resource per deliverable.

#### core

This is the core deliverable the company is profiding, for example a campaign, a tooth brush, a unit of electricity, and so on.

#### revenue

This is the average revenue that is incurred from selling one core unit e.g. a tooth brush.

#### resource

This is the key resource needed in order for the company to be able to produce the core deliverable e.g. a datacenter needs servers.

#### MODEL PARAMETERS

There are several *general aspects* such as the period that should be forecasted.

#### years

The number of years that will be forecasted for the business.

#### tax-rate

A fixed income tax-rate the business is subject to.

#### investment

The total amount of the initial investment into the business. NOTE: this will be the only entry for year-1 and will be added to the 'years' parameter.  

#### depreciation/amortization rate

(missing)

### VOLATILITY PARAMETERS

Each of the three *fundamental aspect* are subject to change each year. A  new growth factor is generated based on three factors.

#### change

The maximum rate of change for the aspect e.g. the maximum rate of change  per annum for revenue is 3 (300%).

#### incertainty

The level of incertainty related with the change e.g. the incertainty of revenue change per annum is 0.9 (90%) where rate of change of 300% would result in 30% to 300% change.

#### steps

The number of steps between the minimum and maximum values for change e.g. in the case of the above example 10 steps would yield possibilities 30%, 60%, 90%...300% and so forth.

## References

[1] https://www.investopedia.com/terms/n/npv.asp

[2] https://hbr.org/2014/11/a-refresher-on-net-present-value
