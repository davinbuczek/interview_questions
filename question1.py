# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

from itertools import permutations
import enchant

d = enchant.Dict('en-US')

def question1(s, t):

    # Check is permutation of t is an anagram
    for value in [''.join(p) for p in permutations(t)]:
        if value in s:
            if d.check(value):
                return True
    return False        

print question1('added', 'da')
  