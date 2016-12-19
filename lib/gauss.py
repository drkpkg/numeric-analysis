from sympy import poly, symbols
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr


class Gauss:
    def __init__(self, args, var):
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

            r = 0
            for k in self.eq_coeffs:
                k[len(k)-1] = int(self.terms[r])
                r += 1

        except TypeError:
            print("Expression cannot be formatted")

    @staticmethod
    def __parse_args(args, equations, terms):
        for i in args:
            actual = i.split('=')
            equations.append(actual[0])
            terms.append(actual[1])

    def solve_gauss(self):
        n = len(self.eq_coeffs)
        for i in range(0, n):
            # Search for maximum in this column
            max_el = abs(self.eq_coeffs[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(self.eq_coeffs[k][i]) > max_el:
                    max_el = abs(self.eq_coeffs[k][i])
                    max_row = k

            # Swap maximum row with current row (column by column)
            for k in range(i, n + 1):
                tmp = self.eq_coeffs[max_row][k]
                self.eq_coeffs[max_row][k] = self.eq_coeffs[i][k]
                self.eq_coeffs[i][k] = tmp

            # Make all rows below this one 0 in current column
            for k in range(i + 1, n):
                c = -self.eq_coeffs[k][i] / self.eq_coeffs[i][i]
                for j in range(i, n + 1):
                    if i == j:
                        self.eq_coeffs[k][j] = 0
                    else:
                        self.eq_coeffs[k][j] += c * self.eq_coeffs[i][j]

        # Solve equation Ax=b for an upper triangular matrix A
        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = self.eq_coeffs[i][n] / self.eq_coeffs[i][i]
            for k in range(i - 1, -1, -1):
                self.eq_coeffs[k][n] -= self.eq_coeffs[k][i] * x[i]
        self.sections = x

    # def is_scaled_matrix(self):
    #     i = 1
    #     is_scaled = False
    #     for row in self.eq_coeffs:
    #         for position in range(len(row) - len(row) + i):
    #             if row[position] == 0:
    #                 is_scaled = True
    #             else:
    #                 is_scaled = False
    #         i += 1
    #     return is_scaled

# if __name__ == '__main__':
#     gauss = Gauss("2x**3+18x**2+4x=1", "x**3+5x**2+x=10", "5x**3+4x**2+9x=9", var='x')
#     gauss.solve_gauss()
#     print(gauss.is_scaled_matrix())
#     print(gauss.sections)
#     print(gauss.eq_coeffs)
