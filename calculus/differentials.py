import sympy as sp

def solve_differential_equation(expression):
    x = sp.symbols('x')
    solution = sp.dsolve(expression)
    return solution

def solve_partial_differential_equation(expression, function):
    solution = sp.pdsolve(expression, function)
    return solution

def solve_first_order_linear_differential_equation(expression):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    equation = y.diff(x) - expression
    solution = sp.dsolve(equation, y)
    return solution

def solve_second_order_linear_differential_equation(expression, y):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    equation = y.diff(x, x) - expression
    solution = sp.dsolve(equation, y)
    return solution

def solve_homogeneous_differential_equation(expression, y):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    equation = y.diff(x) - expression*y
    solution = sp.dsolve(equation, y)
    return solution

def solve_separable_differential_equation(expression1, expression2, y):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    equation = y.diff(x) - expression1*expression2
    solution = sp.dsolve(equation, y)
    return solution
