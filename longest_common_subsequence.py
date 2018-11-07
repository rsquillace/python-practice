import numpy as np
from itertools import combinations

'''
Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

Notes:
Both arguments will be strings
Return value must be a string
Return an empty string if there exists no common subsequence
Both arguments will have one or more characters
All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ), which would have two possible longest common subsequences: "12" and "34".
'''

def find_subsequences(string):

    '''
    Creates a list of all possible subsequences for a string

    INPUT: string
    OUTPUT: list of subsequences of string
    '''

    characters = list(string)
    subsequences = [list(combinations(characters, n)) for n in range(1, len(characters)+1)]
    flattened_subsequences = [item for sublist in subsequences for item in sublist]
    final_subsequences = [''.join(combs) for combs in flattened_subsequences]

    return final_subsequences

def lcs(x, y):

    '''
    Compares list of substrings of two different strings, and returns the longest one in common

    INPUT: two strings
    OUTPUT: longest subsequence shared by the two inputted strings
    '''
    
    x_subsequences = np.array(find_subsequences(x))
    y_subsequences = np.array(find_subsequences(y))
    common_subsequences = np.intersect1d(x_subsequences, y_subsequences)
    if len(common_subsequences) == 0:
        return ''
    else:
        return max(common_subsequences, key=len)
