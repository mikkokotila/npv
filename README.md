![npvpy](https://raw.githubusercontent.com/mikkokotila/npvpy/master/logo.png)

# npvpy
Net Present Value Simulator for Python

## Overview 

npv.py provides a very high level simulation facility for getting the NPV (net presevent value) score for any business idea. By default, the simulation automatically generates an incomes statement based on set of input variables and volatility computations. 

## Use

#### Use with params in a dictionary

    npv = NPV(parameters)
    npv._calculate_npv()
    
#### Use with params in a text file 

    npv = NPV('params.txt')
    npv._calculate_npv()
