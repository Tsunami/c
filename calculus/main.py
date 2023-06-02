import sympy as sp

from derivatives import *
from integrals import *
from differentials import *
from optimization import *
from series import *
from rates import *
from utilities import *

def main():
    while True:
        print("\nChoose a category:")
        print("1. Derivatives")
        print("2. Integrals")
        print("3. Differential Equations")
        print("4. Optimization")
        print("5. Series")
        print("6. Related Rates")
        print("7. Utilities")
        print("8. Exit")

        category = input("Enter your option (1/2/3/4/5/6/7/8): ")

        if category == "8":
            break

        expression = input("Enter the function expression (e.g., 2*x + 3*x**2 - 5*sin(x)): ")
        
        if category == "1":
            print("\n1. Calculate the derivative")
            print("2. Calculate the second derivative")
            print("3. Calculate partial derivative")
            print("4. Calculate derivative at a point")
            option = input("Enter your option (1/2/3/4): ")
    
            if option == "1":
                result = calculate_derivative(expression)
            elif option == "2":
                result = calculate_second_derivative(expression)
            elif option == "3":
                variable = input("Enter the variable with respect to which you want to calculate the partial derivative e.g., y: ")
                result = calculate_partial_derivative(expression, variable)
            elif option == "4":
                point = float(input("Enter the point at which you want to evaluate the derivative e.g., 2: "))
                result = calculate_derivative_at_point(expression, point)

        elif category == "2":
            print("\n1. Calculate the antiderivative")
            print("2. Calculate the definite integral")
            print("3. Calculate the antiderivative at a point")
            print("4. Calculate area under the curve")
            print("5. Calculate volume of solid of revolution")
            print("6. Calculate volume by cylindrical shells")
            option = input("Enter your option (1/2/3/4/5/6): ")
    
            if option == "1":
                result = calculate_antiderivative(expression)
            elif option == "2":
                lower_bound = float(input("Enter the lower bound (a) e.g., -1: "))
                upper_bound = float(input("Enter the upper bound (b) e.g., 1: "))
                result = calculate_definite_integral(expression, lower_bound, upper_bound)
            elif option == "3":
                point = float(input("Enter the point at which you want to evaluate the antiderivative e.g., 2: "))
                result = calculate_antiderivative_at_point(expression, point)
            elif option == "4":
                lower_bound = float(input("Enter the lower bound (a) e.g., -1: "))
                upper_bound = float(input("Enter the upper bound (b) e.g., 1: "))
                result = calculate_area_under_curve(expression, lower_bound, upper_bound)
            elif option == "5":
                lower_bound = float(input("Enter the lower bound (a) e.g., -1: "))
                upper_bound = float(input("Enter the upper bound (b) e.g., 1: "))
                result = calculate_volume_of_solid_of_revolution(expression, lower_bound, upper_bound)
            elif option == "6":
                lower_bound = float(input("Enter the lower bound (a) e.g., -1: "))
                upper_bound = float(input("Enter the upper bound (b) e.g., 1: "))
                result = calculate_volume_by_cylindrical_shells(expression, lower_bound, upper_bound)

        elif category == "3":
            print("\n1. Solve a differential equation")
            print("2. Solve a partial differential equation")
            print("3. Solve a first order linear differential equation")
            print("4. Solve a second order linear differential equation")
            print("5. Solve a homogeneous differential equation")
            print("6. Solve a separable differential equation")
            option = input("Enter your option (1/2/3/4/5/6): ")

            if option == "1":
                result = solve_differential_equation(expression)
            elif option == "2":
                unction = input("Enter the function for the partial differential equation: ")
                result = solve_partial_differential_equation(expression, function)
            elif option == "3":
                result = solve_first_order_linear_differential_equation(expression)
            elif option == "4":
                y = input("Enter the function 'y': ")
                result = solve_second_order_linear_differential_equation(expression, y)
            elif option == "5":
                y = input("Enter the function 'y': ")
                result = solve_homogeneous_differential_equation(expression, y)
            elif option == "6":
                expression1 = input("Enter the first expression for the separable differential equation: ")
                expression2 = input("Enter the second expression for the separable differential equation: ")
                y = input("Enter the function 'y': ")
                result = solve_separable_differential_equation(expression1, expression2, y)

        elif category == "4":
            print("\n1. Find critical points")
            print("2. Find maximum and minimum")
            print("3. Find inflection points")
            print("4. Find concavity")
            option = input("Enter your option (1/2/3/4): ")

            if option == "1":
                result = find_critical_points(expression)
            elif option == "2":
                maximum, minimum = find_max_min(expression)
                result = "Maximum: {}, Minimum: {}".format(maximum, minimum)
            elif option == "3":
                result = find_inflection_points(expression)
            elif option == "4":
                concavity = find_concavity(expression)
                result = ", ".join(["{}: {}".format(point, concave) for point, concave in concavity])

        elif category == "5":
            print("\n1. Calculate the Taylor series expansion")
            print("2. Calculate the power series expansion")
            print("3. Calculate the Fourier series")
            print("4. Calculate the geometric series")
            print("5. Evaluate series at a specific value")
            print("6. Convert series to an expression")
            print("7. Check series convergence with ratio test")
            print("8. Check series convergence with root test")
            option = input("Enter your option (1/2/3/4/5/6/7/8): ")

            if option == "1" or option == "2":
                x_value = float(input("Enter the value of x: "))
                num_terms = int(input("Enter the number of terms (n): "))
                if option == "1":
                    result = calculate_taylor_series(expression, x_value, num_terms)
                else:
                    result = calculate_power_series(expression, x_value, num_terms)
            elif option == "3":
                period = float(input("Enter the period of the function: "))
                result = calculate_fourier_series(expression, period)
            elif option == "4":
                r = float(input("Enter the common ratio (r): "))
                n = int(input("Enter the number of terms (n): "))
                result = calculate_geometric_series(r, n)
            elif option == "5":
                series = input("Enter the series (e.g., x**n/factorial(n)): ")
                x_value = float(input("Enter the value of x: "))
                result = evaluate_series(series, x_value)
            elif option == "6":
                series = input("Enter the series (e.g., x**n/factorial(n)): ")
                result = series_to_expression(series)
            elif option == "7" or option == "8":
                series = input("Enter the series (e.g., x**n/factorial(n)): ")
                if option == "7":
                    result = check_ratio_test(series)
                else:
                    result = check_root_test(series)

        elif category == "6":
            print("\n1. Solve a related rates problem")
            option = input("Enter your option: ")
            if option == "1":
                num_problems = int(input("Enter the number of related rates problems: "))

                expressions = []
                given_rates = []
                given_variables = []
                target_variables = []

                for i in range(num_problems):
                    expression_string = input("Enter the expression for problem {}: ".format(i+1))
                    expressions.append(create_expression(expression_string))

                    given_rate = float(input("Enter the given rate for problem {}: ".format(i+1)))
                    given_rates.append(given_rate)

                    given_variable = input("Enter the given variable for problem {}: ".format(i+1))
                    given_variables.append(given_variable)

                    target_variable = input("Enter the target variable for problem {}: ".format(i+1))
                    target_variables.append(target_variable)

                results = calculate_related_rates(expressions, given_rates, given_variables, target_variables)
                for i, result in enumerate(results):
                    print("Problem {}: {}".format(i+1, result))

        elif category == "7":
            print("\n1. Create an expression")
            print("2. Pretty print an expression")
            print("3. Evaluate an expression")
            print("4. Solve for a variable")
            print("5. Plot an expression")
            print("6. Simplify an expression")
            option = input("Enter your option (1/2/3/4/5/6): ")

            if option == "1":
                expression_string = input("Enter the expression as a string: ")
                expression = create_expression(expression_string)
                print("Expression created:", expression)
            elif option == "2":
                expression_string = input("Enter the expression as a string: ")
                expression = create_expression(expression_string)
                pretty_print(expression)
            elif option == "3":
                expression_string = input("Enter the expression as a string: ")
                expression = create_expression(expression_string)
                variable = input("Enter the variable: ")
                value = float(input("Enter the value of the variable: "))
                result = evaluate_expression(expression, variable, value)
                print("Evaluation result:", result)
            elif option == "4":
                expression_string = input("Enter the expression as a string: ")
                expression = create_expression(expression_string)
                variable = input("Enter the variable to solve for: ")
                result = solve_for_variable(expression, variable)
                print("Solution:", result)
            elif option == "5":
                expression_string = input("Enter the expression as a string: ")
                expression = create_expression(expression_string)
                variable = input("Enter the variable: ")
                start = float(input("Enter the start value: "))
                end = float(input("Enter the end value: "))
                plot_expression(expression, variable, start, end)
            elif option == "6":
                expression_string = input("Enter the expression as a string: ")
                expression = create_expression(expression_string)
                simplified_expression = simplify_expression(expression)
                print("Simplified expression:", simplified_expression)

        else:
            print("Invalid category. Please try again.")
            continue

        print("\nBase Formula: ", expression)
        print("Solution: ", result)

        print("\n====================================")


if __name__ == "__main__":
    main()
