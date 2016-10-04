# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

def question2(a):
    "Returns longest palindromic substring in a given string"
    l=len (a)
    b=a[::-1] # save string length and reverse string
    debug ('string is "{}", reverse is "{}", length is {}'.format (a, b, l))
    for i in xrange (l, 1, -1): # iterate over substring length from largest to smallest
        debug ('substring length is {}'.format (i))
        for j in xrange (0, l-i+1): # iterate of substrings in the given string
            f=a[j:i+j]
            r=b[-i-j:l-j]; # extract forward and reverse substrings
            debug ('offset is {}, forward is {}, reverse is {}'.format (j, f, r))
            if f==r: # return the substring when forward equals reverse
                debug ('longest palindromic substring is {}'.format (f))
                return f
    return ''
    return # empty string when no palindromic substring are found

def debug (message):
    "Prints debugs messages with the option to toggle on and off"
    if False:
        print (message)
        
print question2 ('abcccde'); # 'ccc'
print question2 ('abcccbd'); # 'bcccb'
print question2 ('abedccde'); # 'edccde'
print question2 ('abcccdeed'); # 'deed'
print question2 ('abcccbadeed'); # 'abcccba'
print question2 ('abaccddccefe'); # 'ccddcc'
print question2 ('ABCDEFCBA'); # ''
print question2 ('HYTBCABADEFGHABCDEDCBAGHTFYW1234567887654321ZWETYGDE'); # '1234567887654321'
