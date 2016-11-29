from sympy import poly, symbols
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr


class Gauss:
    def __init__(self, *args, var):
        try:
            self.equations = []
            self.eq_coeffs = []
            self.terms = []
            self.variable = symbols(var)
            self.sections = []
            self.__parse_args(args, self.equations, self.terms)
            transformations = (standard_transformations + (implicit_multiplication_application,))

            for i in range(len(self.equations)):
                self.equations[i] = parse_expr(self.equations[i], transformations=transformations)
                self.equations[i] = poly(self.equations[i])
                self.eq_coeffs.append(self.equations[i].all_coeffs())

        except TypeError:
            print("Expression cannot be formatted")

    @staticmethod
    def __parse_args(args, equations, terms):
        for i in args:
            actual = i.split('=')
            equations.append(actual[0])
            terms.append(actual[1])

    def solve_gauss(self):
        while not self.is_scaled_matrix():
            pass

    def is_scaled_matrix(self):
        i = 1
        is_scaled = False
        for row in self.eq_coeffs:
            for position in range(len(row) - len(row) + i):
                if row[position] == 0:
                    is_scaled = True
                else:
                    is_scaled = False
            i += 1
        return is_scaled

    @staticmethod
    def switch(a, b):
        c = a
        a = b
        b = c

if __name__ == '__main__':
    gauss = Gauss("2x**3 + 18x**2 + 4x = 1", "x**3 + 5x**2 + x = 10", "5x**3 + 4x**2 + 9x = 9", var='x')
    print(gauss.eq_coeffs)
    print(gauss.is_scaled_matrix())
