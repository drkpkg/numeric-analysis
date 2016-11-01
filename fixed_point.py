from equation import Equation


class FixedPoint(Equation):
    def solve_fixed(self, x, error_limit):
        error = 100
        while error > error_limit:
            next_value = float(self.solve(x))
            error = self.get_percentual_error(x, next_value)
            self.sections.append({'x': next_value, 'error': error})
            x = next_value


# fpoint = FixedPoint("E**-x", 'x')
# fpoint.solve_fixed(1, 0.1)
# print(fpoint.sections)
