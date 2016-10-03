from equation import Equation

class Bisection(Equation):

    def getInterval(self,section_a,section_b):
        return ((section_a + section_b)*0.5)

    def solveBisection(self,section_a,section_b,iteration):
        try:
            i = 1
            while i<=iteration:
                interval = self.getInterval(section_a, section_b)
                f_interval = self.solve(interval)
                self.sections.append({'a':section_a,
                                      'b':section_b,
                                      'interval':interval,
                                      'f(interval)':f_interval})
                if f_interval == 0:
                    return f_interval
                else:
                    if self.belowToZero(section_a,interval)==True:
                        section_b = interval
                    else:
                        section_a = interval
                i=i+1
            return interval
        except:
            return "Cannot solve bisection"

if __name__ == '__main__':
    bisection = Bisection("((x)**3)+(4(x)**2)-10",'x')
    print(bisection.solveBisection(1,2,13))
    print(bisection.getSections())