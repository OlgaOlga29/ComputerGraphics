import numpy as np
import math

'''а) Написать функцию, которая для заданной точки плоскости (x, y) формирует матрицу вращения относительно этой 
точки на угол alpha. (x, y, alpha) - параметры функции. '''


def Task1(x, y, alpha):
    R = np.array([[math.cos(alpha), math.sin(-1 * alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    M = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
    M_minus = np.array([[1, 0, -x], [0, 1, -y], [0, 0, 1]])
    result = M.dot(R)
    result = result.dot(M_minus)
    return result


'''б) Написать функцию, которая для заданного треугольника ABC в трехмерном пространстве (xa, ya, za), (xb, yb, zb), 
(xc, yc, zc) определяет вектор нормали к этому треугольнику. (xa, ya, za, xb, yb, zb, xc, yc, zc) - параметры 
функции. '''


def Task2(xa, ya, za, xb, yb, zb, xc, yc, zc):
    ny = (zb - za) * (xc - xa) - (zc - za) * (xb - xa)
    nz = -((yb - ya) * (xc - xa) - (yc - ya) * (xb - xa))
    nx = -(nz * (zb - za) + ny * (yb - ya)) / (xb - xa)
    return nx, ny, nz


'''в) Написать функцию, которая для заданного треугольника ABC в трехмерном пространстве (xa, ya, za), (xb, yb, zb), 
(xc, yc, zc) и точки (x, y) плоскости xOy определяет принадлежит ли точка (x, y) проекции треугольника ABC на 
плоскость xOy. (xa, ya, za, xb, yb, zb, xc, yc, zc, x, y) - параметры функции. '''

def Task3(xa, ya, za, xb, yb, zb, xc, yc, zc, x, y):
    norm1 = (xa - x) * (yb - ya) - (xb - xa) * (ya - y)
    norm2 = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
    norm3 = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)
    return (norm1 < 0) and (norm2 < 0) and (norm3 < 0)


if __name__ == '__main__':
