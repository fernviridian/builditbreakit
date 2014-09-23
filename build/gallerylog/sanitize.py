# -*- coding: utf-8 -*-

# Aug 29, 2014
# rainy_day_hackers
#
# old code was refactored resulting in 10% performance enhancement (raw scores)
# on September 6, 2014

import unicodedata
import string
# import re


# incoming is the argument from parser like an employee name
# or a room-id

# ------------------------------
# returns false if any portion of the incoming string is not 0-9

def sanitizeNumber(incoming):
    zero=ord('0')
    nine=ord('9')
    for item in incoming:
        val=ord(item)
        if val > nine or val < zero:
            return False
    return True

# alternative versions
#    if (re.compile("[^0-9]").search(incoming)):
#        return False #return false if we find anything that isnt alphanumeric
#    else:
#        return True #if it is a valid string, return True
# SLOW
#    newlist=sorted(list(map(ord, incoming)))
#    if (newlist[0] < zero or newlist[-1] > nine):
#        return False
#    return True
# SLOW




# ----------------------------
# returns false if any portion of the incoming string is not
# an ASCII letter

def sanitizeAlpha(incoming):
    capA=ord('A')
    capZ=ord('Z')
    incoming=incoming.upper()
    for item in incoming:
        val=ord(item)
        if val > capZ or val < capA:
            return False
    return True

# alternate versions
# slow
#    if (re.compile("[^a-zA-Z]").search(incoming)):
#        return False #return false if we find anything that isnt alphanumeric
#    else:
#        return True #if it is a valid string, return True
# slow
#    newlist=sorted(list(map(ord, incoming.upper())))
#    if (newlist[0] < capA or newlist[-1] > capZ):
#        return False
#    return True






# ---------------------------------
# returns false if any portion of the incoming string is not
# either an ASCII letter or 0-9

def sanitizeAlphanumeric(incoming):
    zero=ord('0')
    nine=ord('9')
    capA=ord('A')
    capZ=ord('Z')
    incoming=incoming.upper()
    for item in incoming:
        val=ord(item)
        # fix for SSRG_VT/35_invalid_path, woopwoop/team35badpath
        if not((val <= capZ and val >= capA) or (val <= nine and val >= zero)):
            return False
    return True

# alternate versions
# slow
#    if (re.compile("[^0-9a-zA-Z]").search(incoming)):
#        return False #return false if we find anything that isnt alphanumeric
#    else:
#        return True #if it is a valid string, return True
# also slow
#    incoming=list(map(ord, incoming.upper()))
#    for val in incoming:        # no shortcut here since there could be value between 9 and A like @
#        if not((val <= capZ and val >= capA) or (val <= nine and val >= 0)):
#            return False
#    return True


#if __name__=='__main__':
#    alphalist='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'    # string containing only ascii letters
#    numericlist='1234567890'                                            # string containing only numbers
#    alphanumericlist=alphalist+numericlist                              # string containing both
#    mixedbag="')(*  ᕘ ⾜<U+A57D> € ₣'ӓЀ"                                       # random unicode characters
#    print('flag is: {0}, should be True'.format(sanitizeNumber(numericlist)))
#    print('flag is: {0}, should be True'.format(sanitizeAlpha(alphalist)))
#    print('flag is: {0}, should be True'.format(sanitizeAlphanumeric(alphanumericlist)))
#    print('flag is: {0}, should be True'.format(sanitizeAlphanumeric(alphalist)))
#    print('flag is: {0}, should be True'.format(sanitizeAlphanumeric(numericlist)))
#    print('flag is: {0}, should be False'.format(sanitizeNumber(alphalist)))
#    print('flag is: {0}, should be False'.format(sanitizeNumber(alphanumericlist)))
#    print('flag is: {0}, should be False'.format(sanitizeNumber(mixedbag)))
#    print('flag is: {0}, should be False'.format(sanitizeAlpha(alphanumericlist)))
#    print('flag is: {0}, should be False'.format(sanitizeAlpha(numericlist)))
#    print('flag is: {0}, should be False'.format(sanitizeAlpha(mixedbag)))
#    print('flag is: {0}, should be False'.format(sanitizeAlphanumeric(mixedbag)))

