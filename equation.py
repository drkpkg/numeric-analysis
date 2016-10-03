from sympy import symbols
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
import math

class Equation(object):
    def __init__(self, ecuation,variable):
        try:
            transformations = (standard_transformations+(implicit_multiplication_application,))
            self.variable = symbols(variable)
            self.ecuation = parse_expr(ecuation,transformations=transformations)
            self.sections = []
        except:
            return "Expression cannot be formatted"

    def belowToZero(self, section_a, section_b):
        function_from_a = self.solve(section_a)
        function_from_b = self.solve(section_b)
        return (function_from_a*function_from_b < 0)

    def getAbsoluteError(self,actual,last):
        return (actual - last)

    def getPercentualError(self,actual,last):
        return (math.fabs((actual-last)/actual)*100)

    def solve(self, section):
        return self.ecuation.subs({self.variable:section})

    def getExpression(self):
        return self.ecuation

    def getSections(self):
        return self.sections