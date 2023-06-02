import sympy as sp

def calculate_derivative(expression):
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    return derivative

def find_critical_points(expression):
    x = sp.symbols('x')
    derivative = calculate_derivative(expression)
    critical_points = sp.solve(derivative, x)
    return critical_points

def find_max_min(expression):
    x = sp.symbols('x')
    critical_points = find_critical_points(expression)
    maximum = max([expression.subs(x, point) for point in critical_points])
    minimum = min([expression.subs(x, point) for point in critical_points])
    return maximum, minimum

def find_inflection_points(expression):
    x = sp.symbols('x')
    second_derivative = calculate_derivative(calculate_derivative(expression))
    inflection_points = sp.solve(second_derivative, x)
    return inflection_points

def find_concavity(expression):
    x = sp.symbols('x')
    inflection_points = find_inflection_points(expression)
    concavity = []
    for point in inflection_points:
        left_of_point = point - 1
        right_of_point = point + 1
        second_derivative_at_left = calculate_derivative(calculate_derivative(expression)).subs(x, left_of_point)
        second_derivative_at_right = calculate_derivative(calculate_derivative(expression)).subs(x, right_of_point)
        if second_derivative_at_left > 0 and second_derivative_at_right < 0:
            concavity.append((point, 'concave up'))
        elif second_derivative_at_left < 0 and second_derivative_at_right > 0:
            concavity.append((point, 'concave down'))
    return concavity
