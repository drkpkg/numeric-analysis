from sympy import poly, degree, symbols
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr


class Gauss:
    def __init__(self, *args):
        self.equations = []
        self.terms = []

        self.__parse_args(args, self.equations, self.terms)
        print(self.equations, self.terms)

        try:
            transformations = (standard_transformations + (implicit_multiplication_application,))
            self.variable = symbols(self.variable)
            self.dividend = parse_expr(self.polynomial, transformations=transformations)
            self.divider = parse_expr(self.polynomial_divider, transformations=transformations)

            self.polynomial = poly(self.dividend)
            self.polynomial_divider = poly(self.divider)

            self.sections = []
        except:
            return "Expression cannot be formatted"

    @staticmethod
    def __parse_args(args, equations, terms):
        for i in args:
            actual = i.split('=')
            equations.append(actual[0])
            terms.append(actual[1])


if __name__ == '__main__':
    gauss = Gauss("2x = 1", "5y = 10", "4m = 9")
