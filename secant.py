from equation import Equation


class Secant(Equation):
    def solve_secant(self, section_a, section_b, error_limit):
        error = 100
        iteration = 0
        while error > error_limit:
            f_section_a = self.solve(section_a)
            f_section_b = self.solve(section_b)
            new_section = float(section_b - (((section_b - section_a) / (f_section_b - f_section_a)) * f_section_b))

            section_a = section_b
            section_b = new_section

            self.sections.append({'n': iteration, 'x' + str(iteration): new_section, 'error': error})
            error = self.get_percentual_error(section_a, section_b)
            iteration += 1

# if __name__ == '__main__':
#     secant = Secant("x**3+2x**2+10x-20", 'x')
#     secant.solve_secant(0, 1, 0.1)
#     print(secant.get_sections())
