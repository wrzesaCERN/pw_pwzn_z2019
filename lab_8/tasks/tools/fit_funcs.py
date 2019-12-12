import numpy as np
def least_sq(xy):
    x = xy[0]
    y = xy[1]
    n = np.size(x)
    delta = n * np.sum(x*x) - np.sum(x) * np.sum(x)
    b = (np.sum(x * x) * np.sum(y)-np.sum(x * y) * np.sum(x)) / delta
    a = (n * np.sum(x * y)-np.sum(x) * np.sum(y)) / delta
    return (a, b)


