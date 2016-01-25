#!/usr/bin/env python3
"""
Starts a serie generation for logistic series
"""
import logging
import numpy as np


class LogisticSerie(object):
    """
    Numeric logistic serie
    """
    start_value = 0.01
    end_value = 4.0
    precision = 0.001
    k_start = 0.001
    k_end = 4.0

    x0_list = list(np.arange(0.1, 1, 0.1))

    initialized = False

    def __init__(self, **kwargs):
        self.start_value = kwargs.pop('start_value', self.start_value)
        self.end_value = kwargs.pop('end_value', self.end_value)
        self.precision = kwargs.pop('precision', self.precision)

        logging.debug('LogisticSerie() self.start_value = %s / self.end_value = %s / self.precision = %s',
                      self.start_value, self.end_value, self.precision)

    @classmethod
    def get_serie(cls, k, x0=0.2, count=50, **kwargs):
        ls = cls(**kwargs)
        return ls.generate_serie(k, x0, count)

    @staticmethod
    def generate_serie(k, x0=0.2, count=50):
        """
        Generate a serie for a given initial k value

        :param k: k value
        :param x0: initial value for the serie
        :param count: Number of loops
        :returns: serie as a list of tuples (idx, (k, x))
        """
        output = []
        x = x0
        for i in range(count):
            x *= k * (1 - x)
            output.append((i, (k, x)))
        return output

    def generate_series(self, x0, **kwargs):
        k_start = kwargs.pop('k_start', self.k_start)
        k_end = kwargs.pop('k_end', self.k_end)
        precision = kwargs.pop('precision', self.precision)

        output = []
        count = 0
        for k in np.arange(k_start, k_end, precision):
            output.append(self.generate_serie(k, x0))
            count += 1
        logging.info(u'LogisticSerie::generate_series() count = %d', count)
        return output
