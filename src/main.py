#!/usr/bin/env python3
import json
import sys
import logging
import argparse
from collections import OrderedDict
import numpy as np
from matplotlib import pyplot as plt

from logistic_series import LogisticSerie

logging.basicConfig(level=logging.INFO)


def main(*args):
    """
    Main application launcher
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', type=float, help='Start value', action='store', dest='start_value',
                        default=0.1)
    parser.add_argument('-e', '--end', type=float, help='End value', action='store', dest='end_value', default=10.0)
    parser.add_argument('-p', '--precision', type=float, help='Calculation interval', action='store', dest='precision',
                        default=0.001)
    parser.add_argument('-x', type=int, help='Number of plots', dest='x', default=1)
    parser.add_argument('-y', type=int, help='Number of plots', dest='y', default=1)
    parser.add_argument('-i', '--initial-value', type=float, default=0.5, dest='initial_value')

    options = parser.parse_args(*args)
    logging.debug('main() params = %s' % str(options))

    start_value = options.start_value
    end_value = options.end_value
    precision = options.precision
    x = options.x
    y = options.y
    x0 = options.initial_value

    # Initialize series generator
    generator = LogisticSerie(start_value=start_value, end_value=end_value, interval=precision)

    if x == 1 and y == 1:
        generated_series = generator.generate_series(x0=x0)
        # logging.info('serie = %s', json.dumps(generated_series, indent=2))
        get_plot_data(plt, x0, generated_series)
        plt.show()
        input("Type any Enter to exit...")
        return 0

    count = 0
    f, axarr = plt.subplots(x, y)
    count_points = 0
    for x0_val in generator.x0_list:
        # Build series
        generated_series = generator.generate_series(x0=x0_val)
        logging.info('Adding serie for x0 = %s / len(generated_series) = %d', x0_val, len(generated_series))
        logging.debug('[count // 2, count % 2] = [%s, %s]', count // 2, count % 2)

        # Plot initialization
        cur_plt = axarr[count // 3, count % 3]
        get_plot_data(cur_plt, x0_val, generated_series, count)
        logging.info('Total count of points = %s', count_points)
        plt.pause(0.2)
        count += 1

    input('Press Enter key to continue...')

    return 0


def get_plot_data(cur_plt, x0_val, generated_series, count=0, colors=('#003366', 'r', '0.25', 'g')):
    # cur_plt.set_title("Avec X0 = %s" % x0_val)
    cur_plt.axis([0.0, 4.0, 0.0, 1.0])
    for val in np.arange(0, 1.0, 0.2):
        cur_plt.axhline(val, color='b')
    for val in range(4):
        cur_plt.axvline(val, color='b')

    # Zip series as (x0, x1... xn), (y0, y1...yn)
    output = OrderedDict()

    for s in generated_series:
        for data in s:
            i = data[0]
            if i not in output:
                output[i] = ([], [])
            output[i][0].append(data[1][0])
            output[i][1].append(data[1][1])

    # Remove first (straight) serie
    del output[0]

    # Adds dots on plot
    for key, data in output.items():
        logging.debug("key = %s / data = %s", key, data)
        # cur_plt.scatter(data[0], data[1], s=0.5, marker='.', c=colors[count % len(colors)])
        cur_plt.plot(data[0], data[1], c=colors[count % len(colors)], linewidth=0.5, marker=',',
                     linestyle='none')  # s=0.5,


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
