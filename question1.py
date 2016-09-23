# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

from itertools import permutations
import enchant

d = enchant.Dict('en-US')

words = []

def question1(s, t):
    
    perms = [''.join(p) for p in permutations(t)]
    print perms

    # Check is permutation of t is an anagram
    for value in perms:
        if d.check(value):
            words.append(value)

    # Find if anagram is part of s
    for word in words:
        if word in s:
            print 'True'
        else:
            print 'False'                


question1('added', 'da')
  