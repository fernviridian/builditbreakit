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

