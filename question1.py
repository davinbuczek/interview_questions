# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

from itertools import permutations

text = 'test'

perms = [''.join(p) for p in permutations(text)]

print set(perms)