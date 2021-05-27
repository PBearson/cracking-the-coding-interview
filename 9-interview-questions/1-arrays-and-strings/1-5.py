# Given 2 strings, return True if they are 1 edit away.
# Edit means add, remove, or replace a character

# If it is add or remove, then the length difference is 1 and every letter in the smaller appears in the larger, in order
# If it is replace, then the length is the same and every letter in one appears in the other, except for one time

def checkReplace(string1, string2):
    numDiff = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            numDiff += 1
    return numDiff == 1

def checkAddRemove(string1, string2):
    numDiff = 0
    if len(string1) < len(string2):
        minString = string1
        maxString = string2
    else:
        minString = string2
        maxString = string1

    for i in range(len(minString)):
        if minString[i] != maxString[i + numDiff]:
            numDiff += 1
            if numDiff > 1 or minString[i] != maxString[i + numDiff]:
                return False

    return True

def checkOneEditAway(string1, string2):
    lenDiff = abs(len(string1) - len(string2))

    if lenDiff == 0:
        return checkReplace(string1, string2)
    elif lenDiff == 1:
        return checkAddRemove(string1, string2)
    else:
        return False

assert True == checkOneEditAway("pale", "ple")
assert True == checkOneEditAway("pales", "pale")
assert True == checkOneEditAway("pale", "bale")
assert False == checkOneEditAway("pale", "bake")