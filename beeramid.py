import numpy as np

'''
Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

1) your referral bonus, and

2) the price of a beer can
'''


def beeramid(bonus, price):

    '''
    Finds the number of levels possible in the beer pyramid

    INPUT: amount paid in bonus, price of a single beer
    OUTPUT: maximum amount of levels possible with number of beers
    '''
    
    num_beers = bonus/price
    num_levels = 0
    cans_needed_next_level = 1
    while cans_needed_next_level <= num_beers:
        num_levels += 1
        cans_needed_next_level = np.square(num_levels+1)
        num_beers -= np.square(num_levels)

    return num_levels
