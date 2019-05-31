#!/usr/bin/env python
import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='mylog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def factorial(n):
    logging.debug('Start of program')
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    logging.debug('End of program')
    return total


def main():
    # logging.disable(logging.CRITICAL)
    print(factorial(5))


if __name__ == '__main__':
    main()
