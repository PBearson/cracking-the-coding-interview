# Assume we have a call to isSubstring which checks if one word is a substring of another
# Given 2 strings, return True if one is a rotation of another, using only a single call to isSubstring.
# Example:
    # "waterbottle" and "erbottlewat" -> True

# Possible rotations of "waterbottle":
# aterbottlew
# terbottlewa
# erbottlewat
# rbottlewate
# bottlewater
# ottlewaterb
# ttlewaterbo
# tlewaterbot
# lewaterbott
# ewaterbotte

# Walk through the "rotated" string and keep track of the last index where the letters match up contiguously
# Then check if 

def isSubstring(substring, string):
    return substring in string

# Idea: Let the rotation be defined at some point such that the first string is XY
# And the second string is YX (X and Y are substrings)
# If the second string is a truly a rotation, then YXYX will contain XY as a substring, and this 
# will prove that the second string is a rotation. So we can ask if XY is a substring of YXYX.
def isRotation(string1, string2):
    return isSubstring(string1, string2 + string2)

assert True == isRotation("waterbottle", "erbottlewat")
assert True == isRotation("waterbottle", "lewaterbott")
assert True == isRotation("waterbottle", "waterbottle")

assert False == isRotation("waterbottle", "waferbottle")
assert False == isRotation("waterbottle", "bottlawater")
assert False == isRotation("waterbottle", "waterbottll")