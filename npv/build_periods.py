def build_periods(params, aspect):

        '''Handles the generation of data for the three aspect;
        core, revenue, and resource.

        params | dict | the starting parameters for the simulation
        aspect | str | name of the aspect to be generated

        '''

        import numpy as np

        from .change_numbers import change_numbers

        values = []

        change_outcomes = change_numbers(change=params[aspect + '_change'],
                                         incertainty=params[aspect + '_incertainty'],
                                         steps=params[aspect + '_steps'])

        for i in range(params['number_of_months']):
            input_change = np.random.choice(change_outcomes)

            if i == 0:
                input_temp = params[aspect]

            else:
                input_temp = values[i - 1] + (input_change * values[i - 1])

            input_temp = int(input_temp)
            values.append(input_temp)

        return np.array(values)
