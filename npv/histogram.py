import astetik as ast


def histogram(x,
              data,
              color='red',
              bins=20,
              title=None,
              dropna=False):

    '''Helper function to create a distribution histogram
    for `npv.simulate`
    '''

    if dropna is True:
        data.dropna(inplace=True)

    ast.hist(data, data.columns[0], bins=bins)
