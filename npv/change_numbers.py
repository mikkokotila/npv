def change_numbers(change, incertainty, steps):

    '''Handles the computations for generation of data based on
    max change, incertainty of change, and the magnitude of of change.

    change | float or int | a percentile (1 = 100%) of change per period (e.g. month)
    incertainty | float or int | the degree of incertainty with rate of change
    steps | float or int | steps in which growth happens (e.g. deal size)

    '''

    import numpy as np

    change_min = change - (change * incertainty)
    change_max = change + (change * incertainty)
    change_steps = (change_max - change_min) / steps
    change_outcomes = np.arange(change_min, change_max, change_steps)

    return change_outcomes
