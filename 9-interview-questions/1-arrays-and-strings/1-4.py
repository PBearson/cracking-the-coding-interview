# Given a string, return True if it is a permutation of a palindrome
# Example:
    # Input: Tact Coa
    # Output: True (permutation of 'taco cat')
# Ignore casing and non-letter characters

# examples:
# tacocat
# mom
# iamapamai

# If it is a palindrome, we will have an even number of each letter
# Unless there are an odd number of letters, in which case exactly one
# letter will appear an odd number of times

import math

def getStringLength(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    stringLength = 0

    for s in string:
        if s.lower() in alphabet:
            stringLength += 1

    return stringLength

def getLetterFreq(string):
    letterFreq = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for s in string:
        if s.lower() in alphabet:
            if s.lower() not in letterFreq.keys():
                letterFreq[s.lower()] = 1
            else:
                letterFreq[s.lower()] += 1

    return letterFreq

def isPermutationOfPalindrome(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    oddFreqSeen = False

    letterFreq = getLetterFreq(string)

    stringLength = getStringLength(string)

    # Now count frequency of letters
    for a in letterFreq.keys():
        if letterFreq[a] % 2 == 1:
            if stringLength % 2 == 1 and oddFreqSeen == False:
                oddFreqSeen = True
            else:
                return False
    return True

# Assuming we found a permutation of a palindrome, this function will print it out
# Not really expected by the question, but it can help to verify our correctness
def printPalindrome(string):
    if not isPermutationOfPalindrome(string):
        print("%s is not a palindrome" % string)
        return

    letterFreq = getLetterFreq(string)
    stringLength = getStringLength(string)

    palindrome = ["0"] * stringLength

    index = 0

    for k in letterFreq.keys():
        while letterFreq[k] > 0:
            if letterFreq[k] % 2 == 0:
                letterFreq[k] -= 2
            else:
                palindrome[math.floor(stringLength / 2)]
                letterFreq[k] -= 3
            palindrome[index] = k
            palindrome[stringLength - index - 1] = k
            index += 1
    print("".join(palindrome))



assert True == isPermutationOfPalindrome("Tact Coa")
assert False == isPermutationOfPalindrome("BabaCbBL")
assert True == isPermutationOfPalindrome("moOMm")

printPalindrome("Tact Coa")
printPalindrome("BabaCbBL")
printPalindrome("moOMm")