from equation import Equation


class Trapezoidal(Equation):
    def solve_with_simple_trapezoidal(self, a, b):
        fa = self.solve(a)
        fb = self.solve(b)
        result = (b - a) * ((fa + fb) / 2)
        return float(result)

    def solve_with_composed_trapezoidal(self, a, b, n):
        h = (b - a) / (2 * n)
        fa = self.solve(a)
        fb = self.solve(b)
        fab = 0
        sections = self.__calc_sections(a, b, n)

        for i in sections:
            fab = fab + self.solve(i)

        result = h * (fa + (2 * fab) + fb)
        return result

    def __calc_sections(self, a, b, n):
        sections = []
        h = (b - a) / n
        x = a
        for i in range(n - 1):
            x = x + h
            sections.append(x)
        return sections


if __name__ == '__main__':
    trapezoidal = Trapezoidal("x**4", 'x')
    print(trapezoidal.solve_with_simple_trapezoidal(2, 5))
    print(trapezoidal.solve_with_composed_trapezoidal(2, 5, 6))
