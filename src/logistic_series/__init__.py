#!/usr/bin/env python3
"""
Starts a serie generation for logistic series
"""
import sys
import logging
import argparse
from collections import OrderedDict

import numpy as np
from matplotlib import pyplot as plt

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
    parser.add_argument('-i', '--interval', type=float, help='Calculation interval', action='store', dest='interval',
                        default=0.1)

    params = parser.parse_args(*args)
    logging.debug('main() params = %s' % str(params))

    start_value = params.start_value
    end_value = params.end_value
    interval = params.interval

    series = LogisticSerie(start_value=start_value, end_value=end_value, interval=interval)
    colors = ['#003366', 'r', '0.25', 'g']

    count = 0
    f, axarr = plt.subplots(3, 3)
    count_points = 0
    for x0_val in series.x0_list:
        generated_series = series.generate_series(x0=x0_val)
        logging.info('Adding serie for x0 = %s / len(generated_series) = %d', x0_val, len(generated_series))

        logging.debug('[count // 2, count % 2] = [%s, %s]', count // 2, count % 2)

        cur_plt = axarr[count // 3, count % 3]
        cur_plt.set_title("Avec X0 = %s" % x0_val)
        cur_plt.axis([0.0, 4.0, 0.0, 1.0])

        output = OrderedDict()
        for s in generated_series:
            for data in s:
                i = data[0]
                if i not in output:
                    output[i] = ([], [])
                output[i][0].append(data[1][0])
                output[i][1].append(data[1][1])

        del output[0]
        for key, data in output.items():
            logging.debug("key = %s / data = %s", key, data)
            cur_plt.scatter(data[0], data[1], s=0.5, marker='.', c=colors[count % 3])
        logging.info('Total count of points = %s', count_points)
        plt.pause(0.2)
        count += 1

    # plt.show()
    input('Press Enter key to stop...')
    return 0


class LogisticSerie(object):
    """
    Numeric logistic serie
    """
    start_value = 0.01
    end_value = 4.0
    interval = 0.01

    x0_list = list(np.arange(0.1, 1, 0.1))

    initialized = False

    def __init__(self, **kwargs):
        if 'start_value' in kwargs:
            self.start_value = kwargs.pop('start_value')
        if 'end_value' in kwargs:
            self.end_value = kwargs.pop('end_value')
        if 'interval' in kwargs:
            self.interval = kwargs.pop('interval')

        logging.debug('LogisticSerie() self.start_value = %s / self.end_value = %s / self.interval = %s',
                      self.start_value, self.end_value, self.interval)

    @staticmethod
    def generate_serie(k, x0=0.2, count=50):
        output = []
        x = x0
        for i in range(count):
            x = x * k * (1 - x)
            output.append((i, (k, x)))
        return output

    def generate_series(self, x0, start_k=start_value, end_k=end_value, interval=interval):
        output = []
        for k in np.arange(start_k, end_k, interval):
            output.append(self.generate_serie(k, x0))
        return output


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
