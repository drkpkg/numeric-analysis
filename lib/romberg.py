from lib.equation import Equation


class Romberg(Equation):
    def solve_romberg(self, a, b, levels):
        h = b - a
        r = [[0 for x in range(levels + 1)] for y in range(levels + 1)]

        r[0][0] = float(0.5 * h * (self.solve(a) + self.solve(b)))
        m = 1

        for i in range(1, levels + 1):
            h *= 0.5
            m *= 2
            result = 0.0

            for k in range(1, m, 2):
                result = result + self.solve(a + (k * h))

            r[i][0] = float(0.5 * r[i - 1][0] + (result * h))

            n = 1
            for j in range(1, i + 1):
                n *= 4
                r[i][j] = float(r[i][j - 1] + ((r[i][j - 1] - r[i - 1][j - 1]) / (n - 1)))
        return r


# if __name__ == '__main__':
#     romberg = Romberg('(E)**(x)**2', 'x')
#     print(romberg.solve_romberg(0, 1, 5))
