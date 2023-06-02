import sympy as sp

def calculate_taylor_series(expression, x_value, num_terms):
    x = sp.symbols('x')
    taylor_series = expression.series(x, x0=x_value, n=num_terms).removeO()
    return taylor_series

def calculate_power_series(expression, x_value, num_terms):
    x = sp.symbols('x')
    power_series = expression.series(x, x0=x_value, n=num_terms).removeO()
    return power_series

def calculate_fourier_series(expression, period):
    x = sp.symbols('x')
    fourier_series = sp.fourier_series(expression, (x, -period / 2, period / 2))
    return fourier_series

def calculate_geometric_series(r, n):
    x = sp.symbols('x')
    return sp.summation(r**x, (x, 0, n))

def evaluate_series(series, x_value):
    x = sp.symbols('x')
    series_value = series.subs(x, x_value)
    return series_value

def series_to_expression(series):
    return series.as_expr()

def check_ratio_test(series):
    x = sp.symbols('x')
    ratio = sp.limit(series / sp.series(series, x, x0=x+1, n=1), x, sp.oo)
    if abs(ratio) < 1:
        return "The series is absolutely convergent"
    elif abs(ratio) > 1:
        return "The series is divergent"
    else:
        return "The ratio test is inconclusive"

def check_root_test(series):
    x = sp.symbols('x')
    root = sp.limit(abs(series) ** (1/x), x, sp.oo)
    if root < 1:
        return "The series is absolutely convergent"
    elif root > 1:
        return "The series is divergent"
    else:
        return "The root test is inconclusive"
