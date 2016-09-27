# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

from itertools import permutations
import enchant

d = enchant.Dict('en-US')

def question1(s, t):

    for value in [''.join(p) for p in permutations(t)]:
        if value in s:
            if d.check(value):
                return True
    return False        

# Test Case 1 - some anagram of 't' is a substring of 's'
# Should return True
print question1('added', 'da')

# Test Case 2 - some anagram of 't' is NOT a substring of 's'
# Should return False
print question1('udacity', 'ad')

# Test Case 3 - one or both arguments are missing
# Should return error because both arguments need to be present to return 
print question1('added','')  

