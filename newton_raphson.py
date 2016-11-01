from sympy import Eq, diff

from equation import Equation


class NewtonRaphson(Equation):
    def solve_newton(self, x, error_limit):
        error = 100

        while error > error_limit:
            next_value = x - (self.solve(x) / self.solve_derivate(x))
            self.sections.append({'x': next_value, 'error': error})
            error = self.get_percentual_error(x, next_value)
            x = next_value


# newton = NewtonRaphson("cos(x) - x**3", 'x')
# newton.solve_newton(0.5, 0.1)
# print(newton.sections)
# print(newton.derivate_equation)
# print(newton.integrate_equation)
