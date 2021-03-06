from lib.equation import Equation


class FixedPoint(Equation):
    def solve_fixed(self, x, error_limit):
        error = 100
        n = 0
        while True:
            if error <= error_limit:
                break
            next_value = float(self.solve(x))
            error = self.get_percentual_error(x, next_value)
            self.sections.append({'x': str(next_value), 'error': str(error)})
            x = next_value


# if __name__ == '__main__':
#     fpoint = FixedPoint("E**-x", 'x')
#     fpoint.solve_fixed(1, 0.01)
#     print(fpoint.sections)
