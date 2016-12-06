import numpy as np
from sympy import symbols, poly
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr


class Jacobi:
    def __init__(self, *args, limit, var):
        self.limit = limit
        self.variable = symbols(var)
        self.equations = []
        self.terms = []
        self.sections = []
        self.__parse_args(args, self.equations, self.terms)
        transformations = (standard_transformations + (implicit_multiplication_application,))

        self.eq_coeffs = np.zeros(shape=(len(self.equations), len(self.equations)))

        for actual_in_range in range(len(self.equations)):
            self.equations[actual_in_range] = parse_expr(self.equations[actual_in_range],
                                                         transformations=transformations)
            self.equations[actual_in_range] = poly(self.equations[actual_in_range])
            o = self.equations[actual_in_range].coeffs()
            o.reverse()
            i = 0
            for k in range(len(self.eq_coeffs[actual_in_range])):
                self.eq_coeffs[actual_in_range][k] = float(o[i])
                i += 1

    @staticmethod
    def __parse_args(args, equations, terms):
        for actual_index in args:
            actual = actual_index.split('=')
            equations.append(actual[0])
            terms.append(float(actual[1]))

    def solve_jacobi(self):
        coeff_array = np.array(self.eq_coeffs)
        terms_array = np.array(self.terms)

        x = np.zeros_like(terms_array)
        for it_count in range(self.limit):
            x_new = np.zeros_like(x)
            for actual_position in range(coeff_array.shape[0]):
                s1 = np.dot(coeff_array[actual_position, :actual_position], x[:actual_position])
                s2 = np.dot(coeff_array[actual_position, actual_position + 1:], x[actual_position + 1:])
                x_new[actual_position] = (terms_array[actual_position] - s1 - s2) / coeff_array[actual_position, actual_position]

            if np.allclose(x, x_new, atol=1e-10):
                break

            x = x_new
        self.sections = x


# if __name__ == '__main__':
#     jacobi = Jacobi("2x**3+18x**2+4x=1", "x**3+5x**2+x=10", "5x**3+4x**2+9x=9", limit=1000, var='x')
#     print(jacobi.eq_coeffs)
#     jacobi.solve_jacobi()
#     print(jacobi.sections)
