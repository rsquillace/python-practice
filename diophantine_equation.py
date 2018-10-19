import numpy as np

'''
Codewars challenge:

In mathematics, a Diophantine equation is a polynomial equation, usually with two or more unknowns, such that only the integer solutions are sought or studied.

In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form:

x^2 - 4 * y^2 = n
(where the unknowns are x and y, and n is a given positive number) in decreasing order of the positive xi.

If there is no solution return [] or "[]" or "".

'''

def factorizer(num):

    '''
    Creates a list of all factors for the given number

    INPUT: integer
    OUTPUT: list of factors for the inputted number
    '''

    num_factors = []
    for n in range(1, int(np.sqrt(num))+1):
        if num % n == 0:
            factors = [n, int(num/n)]
            num_factors.append(factors)
    return num_factors

def sol_equa(num):

    '''
    Tests all factor pairs to see if, when solved, x and y are integers

    INPUT: integer
    OUTPUT: List of valid x y pairs that solve x^2 - 4 * y^2 = integer

    Note that x^2 - 4 * y^2 = (x - 2y)*(x + 2y) = integer
    Thus, the factors can be set equal to these two parts
    lower_factor = x - 2y
    upper_factor = x + 2y
    which reduces to y = (upper_factor - lower_factor) / 4
    '''

    solutions = []
    num_factors = factorizer(num)
    for factors in num_factors:
        a = factors[0]
        b = factors[1] 
        y = (b - a) / 4
        if y % 1 == 0:
            x = a + (2 * y)
            if x % 1 == 0:
                xy_pair = [int(x), int(y)]
                solutions.append(xy_pair)
    return solutions
