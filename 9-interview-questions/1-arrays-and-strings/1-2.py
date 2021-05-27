# Given 2 strings, return true if 1 is a permutation of the other

# Iterate through string1, store frequency of chars in array
# Iterate through string2, decrement frequency as it is found
# If we see a frequency of 0, return false (means a letter in string2 did not appear in string 1)
def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    all_chars = [0] * 128

    for s in string1:
        s_ascii = ord(s)
        all_chars[s_ascii] += 1

    for s in string2:
        s_ascii = ord(s)
        if all_chars[s_ascii] == 0:
            return False
        all_chars[s_ascii] -= 1
    return True


assert True == isPermutation("abcde", "becad")
assert False == isPermutation("ababab", "baab")
assert False == isPermutation("91023hek", "91024hek")
assert True == isPermutation("GODZILLA!91", "ZILLDOG9!1A")