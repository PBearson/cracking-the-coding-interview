# Check if a string has all unique characters
# What if you cannot use additional data structures?

# Use a data structure
def version1(string):
    chars = {}
    for s in string:
        if s in chars.keys():
            return False
        chars[s] = 1
    return True

# Avoid data structures (well we still use an array but aw well, at least it's O(1) space complexity)
def version2(string):
    all_chars = [0] * 256
    for s in string:
        s_ascii = ord(s)
        if all_chars[s_ascii] == 1:
            return False
        all_chars[s_ascii] = 1
    return True

assert True == version1("ABCDE9!")
assert False == version1("ABCDEA!")
assert True == version2("ABCDE9!")
assert False == version2("ABCDEA!")