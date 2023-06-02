import sympy as sp

def create_expression(expression_string):
    """
    Function to convert a string to a sympy expression.
    """
    x, y, z, t = sp.symbols('x y z t')  # add more symbols as needed
    return sp.sympify(expression_string)


def related_rate(expression, given_rate, given_variable, target_variable):
    derivative = sp.diff(expression, given_variable)

    return derivative.subs(given_variable, given_rate)


def calculate_related_rates(expressions, given_rates, given_variables, target_variables):

    return [related_rate(exp, rate, var, target) for exp, rate, var, target in zip(expressions, given_rates, given_variables, target_variables)]
