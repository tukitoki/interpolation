import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from cubic_spline_2d import *
from lagrange_interpolation_2d import *
from newton_interpolation_2d import *
from scipy.interpolate import lagrange
import numpy as np


def calculate_2d_spline_interpolation(x, y, num=100):
    cubic_spline_2d = CubicSpline2D(x, y)
    params = np.linspace(cubic_spline_2d.params[0], cubic_spline_2d.params[-1], num + 1)[:-1]

    result_x, result_y = [], []
    for param in params:
        point_x, point_y = cubic_spline_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


def calculate_2d_lagrange_polynom(x_points, y_points, num=100):
    lagrange_2d = LagrangeInterpolation2D(x_points, y_points)
    params = np.linspace(lagrange_2d.params[0], lagrange_2d.params[-1], num + 1)
    result_x, result_y = [], []
    for param in params:
        point_x, point_y = lagrange_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


def calculate_2d_newton_polynom(x_points, y_points, num=100):
    newton_2d = NewtonInterpolation2D(x_points, y_points)
    params = np.linspace(newton_2d.params[0], newton_2d.params[-1], num + 1)
    result_x, result_y = [], []
    for param in params:
        point_x, point_y = newton_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


if __name__ == '__main__':
    x_points = []
    y_points = []
    fig, ax = plt.subplots(figsize=(9, 9), num="Cubic Splines Simple App")

    np.seterr(over='raise')

    curve, = ax.plot(x_points, y_points, "-g", label="spline (g)")
    curve_lagrange, = ax.plot(x_points, y_points, "-r", label="lagrange (r)")
    curve_newton, = ax.plot(x_points, y_points, "-m", label="newton (m)")
    points, = ax.plot(x_points, y_points, "x")
    lines = [curve, curve_lagrange, curve_newton]
    rax = plt.axes([0.0, 0.9, 0.1, 0.1])
    labels = [str(line.get_label()) for line in lines]
    visibility = [line.get_visible() for line in lines]
    check = CheckButtons(rax, labels, visibility)

    def on_click(event):
        x_new_point, y_new_point = ax.transData.inverted().transform([event.x, event.y])
        if np.abs(x_new_point) * 16364 > 900 or np.abs(y_new_point) * 16364 > 900:
            return
        x_points.append(x_new_point)
        y_points.append(y_new_point)

        if len(x_points) > 1 and len(x_points) == len(y_points):
            x_curve_points, y_curve_points = calculate_2d_spline_interpolation(x_points, y_points, num=10000)
            x_lagrange_curve_points, y_lagrange_curve_points = calculate_2d_lagrange_polynom(x_points, y_points, num=500)
            x_newton_curve_points, y_newton_curve_points = calculate_2d_newton_polynom(x_points, y_points, num=500)
            curve.set_xdata(x_curve_points)
            curve.set_ydata(y_curve_points)
            curve_lagrange.set_xdata(x_lagrange_curve_points)
            curve_lagrange.set_ydata(y_lagrange_curve_points)
            curve_newton.set_xdata(x_newton_curve_points)
            curve_newton.set_ydata(y_newton_curve_points)

        points.set_xdata(x_points)
        points.set_ydata(y_points)

        fig.canvas.draw()

    def func(label):
        index = labels.index(label)
        lines[index].set_visible(not lines[index].get_visible())
        plt.draw()

    check.on_clicked(func)
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
