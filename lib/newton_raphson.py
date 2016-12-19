from lib.equation import Equation


class NewtonRaphson(Equation):
    def solve_newton(self, x, error_limit):
        error = 100

        while True:
            if error <= error_limit:
                break
            next_value = x - (self.solve(x) / self.solve_derivate(x))
            self.sections.append({'x': str(next_value), 'error': str(error)})
            error = self.get_percentual_error(x, next_value)
            x = next_value


# if __name__ == '__main__':
#     newton = NewtonRaphson("cos(x) - x**3", 'x')
#     newton.solve_newton(0.5, 0.1)
#     print(newton.sections)
