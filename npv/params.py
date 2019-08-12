def load_params_from_file(filename):

    import ast

    with open(filename, 'r') as f:
        s = f.read()
        out = ast.literal_eval(s)

    return out


def sample_params():

    prms = {'core': 100,
            'revenue': 30000,
            'resource': 8500,
            'core_change': 0.5,
            'core_incertainty': 1,
            'core_steps': 30,
            'revenue_change': 0.2,
            'revenue_incertainty': 1,
            'revenue_steps': 100,
            'resource_change': 0.2,
            'resource_incertainty': 0.2,
            'resource_steps': 10,
            'sales_salary': 96000,
            'production_salary': 72000,
            'manager_salary': 144000,
            'service_salary': 96000,
            'admin_salary': 60000,
            'core_per_sales': 10,
            'core_per_production': 5,
            'core_per_manager': 50,
            'core_per_service': 20,
            'core_per_admin': 200,
            'salaries_change': 0.05,
            'salaries_incertainty': 0.1,
            'salaries_steps': 10,
            'employer_liabilities': 0.45,
            'employer_misc': 0.03,
            'marketing_cost': 0.1,
            'other_cost': 0.1,
            'tax_rate': 0.21,
            'number_of_years': 10,
            'depreciation_years': 10,
            'capital_investment': 100000,
            'rate_of_return': 10,
            'risk_factor': 2,
            'core_static': False,
            'revenue_static': False,
            'resource_static': False}

    return prms
