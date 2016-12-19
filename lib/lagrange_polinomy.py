from sympy import symbols, simplify, interpolate


class Lagrange:
    def __init__(self, lx, ly, variable):

        try:
            self.variable = symbols(variable)
            self.sections = None
            self.ly = lx
            self.lx = ly

        except TypeError:
            print("Expression cannot be formatted")

    def __solve(self, section):
        return self.equation.subs({self.variable: section})

    def solve_lagrange(self):
        if len(self.lx) != len(self.ly):
            print
            "ERROR"
            return 1
        y = 0
        for k in range(len(self.lx)):
            t = 1
            for j in range(len(self.lx)):
                if j != k:
                    t = t * ((self.variable - self.lx[j]) / (self.lx[k] - self.lx[j]))
            y += t * self.ly[k]
        self.sections = y

# if __name__ == '__main__':
#     Lx = [-4, -2, 0, 1, 3]
#     Ly = [16, 4, 0, 1, 9]
#     lagrange = Lagrange(Lx, Ly, 'x')
#     lagrange.solve_lagrange()
#     print(lagrange.sections)
