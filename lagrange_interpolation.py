
class LagrangeInterpolation:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        return self.calc_polynomial_at_value(param)

    def calc_polynomial_at_value(self, x):
        polynom = 0
        for index in range(len(self.x)):
            polynom += self.y[index] * self.__calc_basis_polynom(x, index)
        return polynom

    def __calc_basis_polynom(self, x, index):
        polynom = 1
        for x_index in range(len(self.x)):
            if x_index != index:
                polynom *= (x - self.x[x_index]) / (self.x[index] - self.x[x_index])
        return polynom
