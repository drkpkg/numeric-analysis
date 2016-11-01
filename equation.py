from sympy import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
import math


class Equation(object):
    def __init__(self, ecuation, variable):
        try:
            transformations = (standard_transformations + (implicit_multiplication_application,))
            self.variable = symbols(variable)
            self.equation = parse_expr(ecuation, transformations=transformations)
            self.derivate_equation = diff(parse_expr(ecuation, transformations=transformations))
            self.sections = []
        except:
            return "Expression cannot be formatted"

    def below_to_zero(self, section_a, section_b):
        function_from_a = self.solve(section_a)
        function_from_b = self.solve(section_b)
        return function_from_a * function_from_b < 0

    @staticmethod
    def get_absolute_error(actual, last):
        return actual - last

    @staticmethod
    def get_percentual_error(last, actual):
        return math.fabs((actual - last) / actual) * 100

    def solve(self, section):
        return self.equation.subs({self.variable: section})

    def solve_derivate(self, section):
        return self.derivate_equation.subs({self.variable: section})

    def get_expression(self):
        return self.equation

    def get_sections(self):
        return self.sections
