#!/usr/bin/python3.4
import re

# incoming is the argument from parser like an employee name
# or a room-id

# ------------------------------
# returns false if any portion of the incoming string is not 0-9

def sanitizeNumber(incoming):
    if (re.compile("[^0-9]").search(incoming)):
        return False #return false if we find anything that isnt alphanumeric
    else:
        return True #if it is a valid string, return True

# ----------------------------
# returns false if any portion of the incoming string is not
# an ASCII letter

def sanitizeAlpha(incoming):
    if (re.compile("[^a-zA-Z]").search(incoming)):
        return False #return false if we find anything that isnt alphanumeric
    else:
        return True #if it is a valid string, return True

# ---------------------------------
# returns false if any portion of the incoming string is not
# either an ASCII letter or 0-9

def sanitizeAlphanumeric(incoming):
    if (re.compile("[^0-9a-zA-Z]").search(incoming)):
        return False #return false if we find anything that isnt alphanumeric
    else:
        return True #if it is a valid string, return True



# alphalist='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'    # string containing only ascii letters
# numericlist='1234567890'                                            # string containing only numbers
# alphanumericlist=alphalist+numericlist                              # string containing both
# mixedbag="')(*  ᕘ ⾜<U+A57D> € ₣'ӓЀ"                                       # random unicode characters
#
# print('flag is: {0}, should be True'.format(sanitizeNumber(numericlist)))
# print('flag is: {0}, should be True'.format(sanitizeAlpha(alphalist)))
# print('flag is: {0}, should be True'.format(sanitizeAlphanumeric(alphanumericlist)))
# print('flag is: {0}, should be True'.format(sanitizeAlphanumeric(alphalist)))
# print('flag is: {0}, should be True'.format(sanitizeAlphanumeric(numericlist)))
# print('flag is: {0}, should be False'.format(sanitizeNumber(alphalist)))
# print('flag is: {0}, should be False'.format(sanitizeNumber(alphanumericlist)))
# print('flag is: {0}, should be False'.format(sanitizeNumber(mixedbag)))
# print('flag is: {0}, should be False'.format(sanitizeAlpha(alphanumericlist)))
# print('flag is: {0}, should be False'.format(sanitizeAlpha(numericlist)))
# print('flag is: {0}, should be False'.format(sanitizeAlpha(mixedbag)))
# print('flag is: {0}, should be False'.format(sanitizeAlphanumeric(mixedbag)))

