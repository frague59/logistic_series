import sys
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)


def main(*args):
    """
    Main application launcher
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', type=float, help='Start value', action='store', dest='start_value',
                        default=0.0)
    parser.add_argument('-e', '--end', type=float, help='End value', action='store', dest='end_value', default=10.0)
    parser.add_argument('-i', '--interval', type=float, help='Calculation interval', action='store', dest='interval',
                        default=0.01)

    params = parser.parse_args(*args)
    logging.debug('main() params = %s' % str(params))

    start_value = params.start_value
    end_value = params.end_value
    interval = params.interval

    serie = LogisticSerie(start_value=start_value, end_value=end_value, interval=interval)

    return 0


class LogisticSerie(object):
    """
    Numeric logistic serie
    """
    start_value = 0.0
    end_value = 10.0
    interval = 0.01

    def __init__(self, **kwargs):
        if 'start_value' in kwargs:
            self.start_value = kwargs.pop('start_value')
        if 'end_value' in kwargs:
            self.end_value = kwargs.pop('end_value')
        if 'interval' in kwargs:
            self.interval = kwargs.pop('interval')

        logging.debug('LogisticSerie() self.start_value = %s / self.end_value = %s / self.interval = %s',
                      self.start_value, self.end_value, self.interval)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))