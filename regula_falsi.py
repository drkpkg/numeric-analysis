from sympy import Eq

from equation import Equation

class RegulaFalsi(Equation):

    def solveRegula(self, a, b, error):
        x = 0
        while(True):
            x = self.getInterval(a, b)
            if x == 0:
                break
            else:
                if self.belowToZero(a,x):
                    b = x
                else:
                    a = x
            print(str(x))

            if self.getPercentualError(a,b) < error:
                break
        return x

    def getInterval(self, a, b):
        return (Eq(self.solve(a) * b) - (self.solve(b) * a)) / (self.solve(a) - self.solve(b))


if __name__ == '__main__':
    falsi = RegulaFalsi("(e**-x)-ln(x)","x")
    falsi.solveRegula(1,2,1)
