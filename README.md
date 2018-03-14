![npvpy](https://raw.githubusercontent.com/mikkokotila/npvpy/master/logo.png)

# npvpy
Net Present Value Simulator for Python

## 1. Overview 

npv.py provides a very high level simulation facility for getting the NPV (net presevent value) score for any business idea. By default, the simulation automatically generates an incomes statement based on set of input variables and volatility computations. 

### 1.1. About NPV

NPV is widely used by managers and investors to support decision making on large investments. For long it has been the gold standard tool for merger and acquisition activity, but is referred to as the 'discounted cash flow model' in that context. In fact, NPV is the model that Warren Buffet uses to evaluate companies[1]. 

## 2. Install and Use

### 2.1 Install 

to install: 

    pip install git+https://github.com/mikkokotila/npvpy.git

### 2.2. Use

#### To import

    from npvpy.main import NPV

#### Use with params in a dictionary

    npv = NPV(parameters)
    npv._calculate_npv()
    
#### Use with params in a text file 

    npv = NPV('params.txt')
    npv._calculate_npv()

## 3. Parameters

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

[1] https://hbr.org/2014/11/a-refresher-on-net-present-value
