import warnings
import pandas as pd
import numpy as np

from npvpy.main import NPV
from npvpy.dist import dist

def simulate(rounds, parameters, df=False, distribution=True):
    
    '''NPV Simulator
    rounds =     the number of times simulation
                 will be run
                 
    parameters = either a dictionary, or filename
                 in string format.
    
    '''
    
    npv = NPV(parameters)
    
    out = []
    
    for i in range(rounds):
        score = npv._calculate_npv()
        out.append(score)
    
    if df is True:
        out = pd.DataFrame(out)
        out.columns = ['NPV']
    
    else:
        out = np.array(out)
        
    if distribution is True:
        if df is False:
            out = pd.DataFrame(out)
            out.columns = ['NPV']
         
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            dist('NPV', out, bins=50)
            
    return out
