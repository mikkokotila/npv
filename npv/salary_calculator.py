def salary_calculator(params, cores):

    from math import ceil
    import numpy as np

    from .change_numbers import change_numbers

    staff_cost = []
    head_count = []

    aspect = 'salaries'
    change_outcomes = change_numbers(change=params[aspect + '_change'],
                                         incertainty=params[aspect + '_incertainty'],
                                         steps=params[aspect + '_steps'])

    for i in range(params['number_of_months']):

        # establishing individual values

        sales_head = ceil(cores[i] / params['core_per_sales'])
        production_head = ceil(cores[i] / params['core_per_production'])
        manager_head = ceil((cores[i] / params['core_per_manager']))
        service_head = ceil((cores[i] / params['core_per_service']))
        admin_head = ceil((cores[i] / params['core_per_admin']))

        sales_total = params['sales_salary'] * sales_head
        production_total = params['production_salary'] * production_head
        manager_total = params['manager_salary'] * manager_head
        service_total = params['service_salary'] * service_head
        admin_total = params['admin_salary'] * admin_head

        # summing up the individual values
        salaries_total = sales_total + production_total + \
            manager_total + service_total + admin_total

        # getting the growth factor
        input_growth = np.random.choice(change_outcomes)

        if i == 0:
            staff_temp = salaries_total + \
                (salaries_total * (params['employer_liabilities'] + params['employer_misc']))
        else:
            staff_temp = salaries_total + \
                (salaries_total * (params['employer_liabilities'] + params['employer_misc']))
            staff_temp = staff_temp + (staff_temp * input_growth)

        head_count.append([sales_head,
                           production_head,
                           manager_head,
                           service_head,
                           admin_head])

        staff_cost.append(int(staff_temp))

    return np.array(staff_cost), np.array(head_count)
