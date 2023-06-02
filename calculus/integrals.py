import sympy as sp

def calculate_antiderivative(expression):
    x = sp.symbols('x')
    antiderivative = sp.integrate(expression, x)
    return antiderivative

def calculate_definite_integral(expression, lower_bound, upper_bound):
    x = sp.symbols('x')
    definite_integral = sp.integrate(expression, (x, lower_bound, upper_bound))
    return definite_integral

def calculate_antiderivative_at_point(expression, point):
    x = sp.symbols('x')
    antiderivative = sp.integrate(expression, x)
    antiderivative_at_point = antiderivative.subs(x, point)
    return antiderivative_at_point

def calculate_area_under_curve(expression, lower_bound, upper_bound):
    x = sp.symbols('x')
    area = sp.integrate(sp.Abs(expression), (x, lower_bound, upper_bound))
    return area

def calculate_volume_of_solid_of_revolution(expression, lower_bound, upper_bound):
    x = sp.symbols('x')
    volume = sp.integrate(sp.pi * expression**2, (x, lower_bound, upper_bound))
    return volume

def calculate_volume_by_cylindrical_shells(expression, lower_bound, upper_bound):
    x = sp.symbols('x')
    volume = sp.integrate(2 * sp.pi * x * expression, (x, lower_bound, upper_bound))
    return volume
