#!/usr/bin/python3.4

import unicodedata          # for ord

# incoming is the argument from parser like an employee name
# or a room-id

# ------------------------------
# returns false if any portion of the incoming string is not 0-9

def sanitize_number(incoming):
    lower = hex(ord('0'))                       # 0 hex 30
    upper = hex(ord('9'))                       # 9 hex 39
    flag = True                                 # valid incoming
    for symbol in incoming:
        symbol = hex(ord(symbol))               # change the symbol to hex
        if symbol < lower or symbol > upper:    # either is out of range
            flag = False
    return flag

# ----------------------------
# returns false if any portion of the incoming string is not
# an ASCII letter

def sanitize_alpha(incoming):
    lower = hex(ord('A'))                       # A = 0x41
    upper = hex(ord('Z'))                       # Z = 0x5A
    incoming = incoming.upper()                 # make caps
    flag = True                                 # valid incoming
    for symbol in incoming:
        symbol = hex(ord(symbol))               # change the symbol to hex
        if symbol < lower or symbol > upper:    # either is out of range
            flag = False
    return flag

# ---------------------------------
# returns false if any portion of the incoming string is not
# either an ASCII letter or 0-9

def sanitize_alphanumeric(incoming):
    lower = hex(ord('0'))                       # 0 hex 30
    upper = hex(ord('9'))                       # 9 hex 39
    lowerA = hex(ord('A'))                      # A = 0x41
    upperZ = hex(ord('Z'))                      # Z = 0x5A
    incoming = incoming.upper()                 # make caps
    flag = True                                 # valid incoming
    for symbol in incoming:
        symbol = hex(ord(symbol))               # change the symbol to hex
        if not ((symbol >= lowerA and symbol <= upperZ) or (symbol >= lower and symbol <= upper)):    # either is out of range
            flag = False
    return flag

# --------------------------------
#


