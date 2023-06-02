import sympy as sp

def create_expression(expression_string):
    x, y, z, t = sp.symbols('x y z t')  # add more symbols as needed
    return sp.sympify(expression_string)

def pretty_print(expression):
    sp.init_printing(use_unicode=True)
    sp.pprint(expression)

def evaluate_expression(expression, variable, value):
    return expression.subs(variable, value)

def solve_for_variable(expression, variable):
    return sp.solve(expression, variable)

def plot_expression(expression, variable, start, end):
    sp.plot(expression, (variable, start, end))
