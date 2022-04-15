
class NewtonInterpolation:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        polynom = 0
        for index in range(len(self.x)):
            polynom += self.__calc_argument(index + 1) * self.__calc_difference_product(index, param, -1)
        return polynom

    def __calc_argument(self, index):
        argument = 0
        for i in range(0, index):
            argument += self.y[i] / self.__calc_difference_product(index, self.x[i], i)
        return argument

    def __calc_difference_product(self, index, value, except_index):
        product = 1
        for x_index in range(0, index):
            if x_index != except_index:
                product *= value - self.x[x_index]
        return product
