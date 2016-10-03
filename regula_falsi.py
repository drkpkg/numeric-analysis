from equation import Equation

class RegulaFalsi(Equation):

    def solveRegula(self, a, b):
        x = 0
        for i in range(10):
            x = self.getInterval(a, b)
            if x == 0:
                break
            else:
                if self.belowToZero(a,x):
                    b = x
                else:
                    a = x
            print(str(x))
        return x

    def getInterval(self, a, b):
        return (float(self.solve(a) * b) - (self.solve(b) * a)) / (self.solve(a) - self.solve(b))


if __name__ == '__main__':
    falsi = RegulaFalsi("(2x**3)-(4x**2)+3x","x")
    falsi.solveRegula(-1,1)
