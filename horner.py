from sympy import poly, degree, symbols, Symbol, Poly
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr

class Horner:
    def __init__(self, polynomial, polynomial_divider, variable):
        try:
            transformations = (standard_transformations + (implicit_multiplication_application,))
            self.variable = symbols(variable)
            self.dividend = parse_expr(polynomial, transformations=transformations)
            self.divider = parse_expr(polynomial_divider, transformations=transformations)

            self.polynomial = poly(self.dividend)
            self.polynomial_divider = poly(self.divider)

            self.quotient = None
            self.residue = None
            self.sections = []
        except:
            return "Expression cannot be formatted"

    def get_degree(self, pol):
        return degree(pol, self.variable)

    def solve_horner(self):
        dividend = self.polynomial.all_coeffs()
        divider = self.inverted_poly()
        position_dividend = 1
        distance = len(dividend)-(len(divider)-1)
        i = 0

        while i < distance:
            d = dividend[i] / divider[0]
            self.sections.append(d)

            position_divider = 1
            while position_divider < len(divider):
                dividend[position_dividend] = dividend[position_dividend] + (d * divider[position_divider])
                position_divider += 1
                position_dividend += 1
            position_dividend -= 1
            i += 1

        self.quotient = self.parse_poly(dividend[0:distance])
        self.residue = self.parse_poly(dividend[distance:len(dividend)])

    @staticmethod
    def parse_poly(data):
        x = Symbol('x')
        return Poly.from_list(data, gens=x)

    def inverted_poly(self):
        h = self.polynomial_divider.all_coeffs()
        new = [h[0]]
        counter = 1
        while counter < len(h):
            new.append(h[counter] * -1)
            counter += 1
        return new


# horner = Horner("38x**4-65x**3+0x**2+0x+27", "2x**2-5x+3", 'x')
# print(horner.solve_horner())

horner = Horner("8x**5+14x**4+5x**3+16x**2+3x+2", "4x**2+x+3", 'x')
horner.solve_horner()
print(horner.quotient, horner.residue)
