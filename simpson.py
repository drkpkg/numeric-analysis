from equation import Equation


class Simpson(Equation):
    def solve_with_simple_simpson(self, a, b):
        ba = (b - a) / 6
        fa = self.solve(a)
        fab = self.solve((a + b) / 2)
        fb = self.solve(b)
        result = ba * (fa + (4 * fab) + fb)
        return float(result)

    def solve_with_3_8_simpson(self, a, b, n):
        h = (b - a) / n
        fa = self.solve(a)
        fb = self.solve(b)
        fab = 0

        for i in range(1, n):
            fab = fab + self.solve(a+(i*h))

        result = ((3/8)*h)*(fa + (3 * fab) + fb)
        return float(result)

if __name__ == '__main__':
    # simpson = Simpson("(2x+3)/(x**2+3x+2)", 'x')
    simpson = Simpson("(x(E**(3x)))", 'x')
    print(simpson.solve_with_simple_simpson(0, 1))
    print(simpson.solve_with_3_8_simpson(0, 1, 3))
