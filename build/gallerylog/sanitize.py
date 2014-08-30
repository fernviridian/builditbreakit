#!/usr/bin/python3.4

import unicodedata          # for ord

# incoming is the argument from parser like an employee name
# or a room-id

# ------------------------------
# returns false if any portion of the incoming string is not 0-9

def sanitize_number(incoming):
    lower = 0x30                                # 0
    upper = 0x39                                # 9
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
    lower = 0x41                                # A
    upper = 0x5A                                # Z
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
    lower = 0x30                                # 0
    upper = 0x39                                # 9
    lowerA = 0x41                               # A
    upperA = 0x5A                               # Z
    incoming = incoming.upper()                 # make caps
    flag = True                                 # valid incoming
    for symbol in incoming:
        symbol = hex(ord(symbol))               # change the symbol to hex
        if not ((symbol >= lowerA and symbol <= upperB) or (symbol >= lower and symbol <= upper)):    # either is out of range
            flag = False
    return flag

# --------------------------------
#


