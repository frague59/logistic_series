import sys
import logging
import math
import matplotlib

matplotlib.use('tkagg')
from matplotlib import pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG)


def main(args):
    sin_x, sin_y = [], []
    cos_x, cos_y = [], []
    plt.axis([-7, 7, -1.1, 1.1])
    for x in np.arange(-2 * math.pi, 2 * math.pi, 0.001):
        y = np.sin(x)
        sin_x.append(x)
        sin_y.append(y)
        y = np.cos(x)
        cos_x.append(x)
        cos_y.append(y)
    plt.plot(sin_x, sin_y)
    plt.plot(cos_x, cos_y)

    plt.show()
    input('Strike ay key when ready...')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
