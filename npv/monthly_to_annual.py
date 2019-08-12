def monthly_to_annual(monthly_data):

    '''Converts monthly data to annual'''

    import pandas as pd
    import numpy as np

    monthly = monthly_data.values
    years = int(monthly_data.shape[1] / 12)
    start = 0
    end = 11

    for year in range(years):

        to_year = monthly[:, start:end].sum(axis=1)

        if year == 0:
            annual = np.array(to_year)
        else:
            annual = np.vstack([annual, to_year])

        start += 12
        end += 12

    annual = pd.DataFrame(annual).transpose()
    annual.index = monthly_data.index

    return annual
