#!/usr/bin/env python3
"""
Simple tests for Tk plot display
"""
import sys
import logging
import math
import matplotlib

matplotlib.use('tkagg')
from matplotlib import pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG)

def main(args):
    val_x, sin_y, cos_y, tan_y = [], [],[],[],
    plt.axis([-2*np.pi, 2*np.pi, -10, 10])
    labels = ['-2*π', '-5/3*π','-4/3*π','-π','-2/3*π', '-1/3*π', '0',
    	      '1/3*π', '2/3*π', 'π', '4/3*π', '5/3*π', '2π']
    plt.xticks(np.arange(-2*np.pi, 2*np.pi + 0.01, np.pi / 3), labels)
    plt.axhline(0, color='b')
    plt.axhline(-1, color='0.25')
    plt.axhline(1, color='0.25')

    plt.axvline(0, color='black')

    for x in np.arange(-2 * math.pi, 2 * math.pi, 0.001):
        val_x.append(x)
        y = np.sin(x)
        sin_y.append(y)
        y = np.cos(x)
        cos_y.append(y)
        y = np.tan(x)
        tan_y.append(y)

    plt.plot(val_x, sin_y)
    plt.plot(val_x, cos_y)
    plt.plot(val_x, tan_y)

    plt.show()
    # input('Strike ay key when ready...')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
