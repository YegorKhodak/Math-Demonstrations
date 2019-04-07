import numpy as np
import matplotlib.pyplot as plt


def rotate_set(theta, x, y):
    # rotation matrix
    T = np.matrix([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])
    new_x = []
    new_y = []
    for i in range(len(x)):
        point = np.dot(T, np.array([x[i], y[i]]))
        new_x.append(point[0, 0])
        new_y.append(point[0, 1])
    return new_x, new_y


def main_loop(x, y, theta):
    while True:
        axes = plt.gca()
        axes.set_xlim([-3, 3])
        axes.set_ylim([-3, 3])
        x, y = rotate_set(theta, x, y)
        X = x[:]
        Y = y[:]
        for i in range(len(Y) - 1):
            for j in range(len(Y) - 1 - i):
                if Y[j] < Y[j + 1]:
                    Y[j], Y[j + 1] = Y[j + 1], Y[j]
                    X[j], X[j + 1] = X[j + 1], X[j]

        for i in range(len(Y)):
            plt.plot(X[i: i+2], Y[i: i+2], 'ro-')

        plt.plot([X[0], X[-1]], [Y[0], Y[-1]], 'bo-')
        plt.pause(0.01)
        plt.clf()


if __name__ == "__main__":
    set_size = 20
    # np.random.seed(seed=1)
    _x = np.random.normal(0, 1, size=set_size)

    # np.random.seed(seed=5)
    _y = np.random.normal(0, 1, size=set_size)

    _theta = 0.05

    main_loop(_x, _y, _theta)
