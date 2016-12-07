from equation import Equation


class Finite(Equation):
    def solve_finite_up(self, x, h):
        self.__calc_sections(x, h)
        f = (self.fx[2] - self.fx[0]) / h
        return f

    def solve_finite_down(self, x, h):
        self.__calc_sections(x, h)
        f = (self.fx[1] - self.fx[0]) / h
        return f

    def solve_finite_central(self, x, h):
        self.__calc_sections(x, h)
        f = (self.fx[2] - self.fx[0]) / h
        return f

    def __calc_sections(self, x, h):
        self.x = [x - h, x, x + h]
        self.fx = []

        for k in self.x:
            self.fx.append(float(self.solve(k)))

if __name__ == '__main__':
    finite = Finite("(sin(x)+(x**2)-2x)/(x**2+1)", 'x')
    print(finite.solve_finite_down(4, 0.2))
    print(finite.solve_finite_up(4, 0.2))
    print(finite.solve_finite_central(4, 0.2))
