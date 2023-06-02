import sympy as sp

def calculate_derivative(expression):
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    return derivative

def calculate_second_derivative(expression):
    x = sp.symbols('x')
    second_derivative = sp.diff(expression, x, x)
    return second_derivative

def calculate_partial_derivative(expression, variable):
    derivative = sp.diff(expression, variable)
    return derivative

def calculate_derivative_at_point(expression, point):
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    derivative_at_point = derivative.subs(x, point)
    return derivative_at_point
