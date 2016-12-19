from lib.equation import Equation


class Bisection(Equation):

    @staticmethod
    def get_interval(section_a, section_b):
        return (section_a + section_b) * 0.5

    def solve_bisection(self, section_a, section_b, error_limit):
        try:
            error = 100
            while error >= error_limit:
                interval = self.get_interval(section_a, section_b)
                f_interval = self.solve(interval)
                error = self.get_percentual_error(section_a, section_b)
                self.sections.append({'a': str(section_a),
                                      'b': str(section_b),
                                      'interval': str(interval),
                                      'f(interval)': str(f_interval),
                                      'error': str(error)})
                if f_interval == 0:
                    return f_interval
                else:
                    if self.below_to_zero(section_a, interval):
                        section_b = interval
                    else:
                        section_a = interval
        except TypeError:
            print("Expression cannot be formatted")


# if __name__ == '__main__':
#     bisection = Bisection("((x)**3)+(4(x)**2)-10", 'x')
#     bisection.solve_bisection(1, 2, 0.02)
#     print(bisection.derivate_equation)
#     print(bisection.get_sections())
