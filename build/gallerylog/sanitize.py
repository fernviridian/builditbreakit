#!/usr/bin/python3.4

import unicodedata          # for ord

# incoming is the argument from parser like an employee name
# or a room-id

# ------------------------------
# returns false if any portion of the incoming string is not 0-9

def sanitize_number(incoming):
    lower = ord('0')                         # 0  30
    upper = ord('9')                         # 9  39
    flag = True                                     # valid incoming
#    count = 0;                          # testing
    for symbolorig in incoming:
        symbol = ord(symbolorig)         # change the symbol to int
        if symbol < lower or symbol > upper:    # either is out of range
            flag = False
#            count += 1                  # testing
#        else:                           # testing
#            print(symbolorig, symbol)   # testing
#    print('{0} flags vs. {1} characters'.format(count, len(incoming)))    # testing
    return flag

# ----------------------------
# returns false if any portion of the incoming string is not
# an ASCII letter

def sanitize_alpha(incoming):
    lower = ord('A')                     # A = 0x41
    upper = ord('Z')                     # Z = 0x5A
    incoming = incoming.upper()                 # make caps
    flag = True                                 # valid incoming
#    count = 0;                          # testing
    for symbolorig in incoming:
        symbol = ord(symbolorig)         # change the symbol to int
        if symbol < lower or symbol > upper:    # either is out of range
            flag = False
#            count += 1                  # testing
#        else:                           # testing
#            print(symbolorig, symbol)   # testing
#    print('{0} flags vs. {1} characters'.format(count, len(incoming)))    # testing
    return flag

# ---------------------------------
# returns false if any portion of the incoming string is not
# either an ASCII letter or 0-9

def sanitize_alphanumeric(incoming):
    lower = ord('0')                     # 0  30
    upper = ord('9')                     # 9  39
    lowerA = ord('A')                    # A = 0x41
    upperZ = ord('Z')                    # Z = 0x5A
    incoming = incoming.upper()                 # make caps
    flag = True                                 # valid incoming
#    count = 0;                          # testing
    for symbolorig in incoming:
        symbol = ord(symbolorig)               # change the symbol to int
        if not ((symbol >= lowerA and symbol <= upperZ) or (symbol >= lower and symbol <= upper)):    # either is out of range
            flag = False
#            count += 1                  # testing
#        else:                           # testing
#            print(symbolorig, symbol)   # testing
#    print('{0} flags vs. {1} characters'.format(count, len(incoming)))    # testing
    return flag

# --------------------------------
#   testing


# alphalist='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'    # string containing only ascii letters
# numericlist='1234567890'                                            # string containing only numbers
# alphanumericlist=alphalist+numericlist                              # string containing both
# mixedbag="')(*  ᕘ ⾜ꕽ € ₣'ӓЀ"                                       # random unicode characters
#
# print('flag is: {0}, should be True'.format(sanitize_number(numericlist)))
# print('flag is: {0}, should be True'.format(sanitize_alpha(alphalist)))
# print('flag is: {0}, should be True'.format(sanitize_alphanumeric(alphanumericlist)))
# print('flag is: {0}, should be True'.format(sanitize_alphanumeric(alphalist)))
# print('flag is: {0}, should be True'.format(sanitize_alphanumeric(numericlist)))
# print('flag is: {0}, should be False'.format(sanitize_number(alphalist)))
# print('flag is: {0}, should be False'.format(sanitize_number(alphanumericlist)))
# print('flag is: {0}, should be False'.format(sanitize_number(mixedbag)))
# print('flag is: {0}, should be False'.format(sanitize_alpha(alphanumericlist)))
# print('flag is: {0}, should be False'.format(sanitize_alpha(numericlist)))
# print('flag is: {0}, should be False'.format(sanitize_alpha(mixedbag)))
# print('flag is: {0}, should be False'.format(sanitize_alphanumeric(mixedbag)))
