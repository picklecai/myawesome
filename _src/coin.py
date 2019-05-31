#!/usr/bin/env python
# _*_coding:utf-8_*_

import random
import logging


def guess_toss():
    logging.debug('Start of debug the function named guess_toss.')
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails: ')
        guess = input()
        logging.debug('You put a guess: %s' % (guess))
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    if toss == 1:
        toss = 'heads'
    else:
        toss = 'tails'
    logging.debug('The game genrerate a toss: %s' % (toss))
    if toss == guess:
        logging.debug('%s == %s is %s' % (toss, guess, toss == guess))
        print('You got it.')
    else:
        logging.debug('%s == %s is %s' % (toss, guess, toss == guess))
        print('Nope! Guess again.')
        guess = input()
        logging.debug('You guess again for: %s ' % (guess))
        if toss == guess:
            print('You got it!')
            logging.debug('%s == %s is %s' % (toss, guess, toss == guess))
        else:
            print('None. You are really bad at this game.')
            logging.debug('%s == %s is %s' % (toss, guess, toss == guess))
    logging.debug('End of debug of function named guess_toss.\n')
    return


def main():
    level = logging.DEBUG
    format1 = ' %(asctime)s - %(levelname)s - %(message)s'
    filename = 'coin_log.txt'
    logging.basicConfig(filename=filename, level=level, format=format1)
    # logging.basicConfig(level=level, format=format1)
    guess_toss()

if __name__ == '__main__':
    main()
