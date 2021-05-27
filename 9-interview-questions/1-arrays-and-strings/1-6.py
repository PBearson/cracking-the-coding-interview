# Implement a compression method of the following form:
# "aabcccccaaa" -> "a2b1c5a3"
# If the compressed string is not smaller, return the original string
# Assume only uppercase and lowercase letters

import time

def compress(string):
    compressedString = ""
    candidate = string[0]
    candidateFreq = 1

    # When we hit the last char of the string or the next char is different
    for i in range(1, len(string)):
        s = string[i]
        if s != candidate:
            compressedString = compressedString + candidate + str(candidateFreq)
            candidateFreq = 1
            candidate = s
        else:
            candidateFreq += 1
    
    compressedString = compressedString + candidate + str(candidateFreq)

    if len(compressedString) >= len(string):
        return string
    else:
        return compressedString

# This time we use a list instead of a string, so we avoid string concatenation
def compressv2(string):
    compressedString = []
    candidate = string[0]
    candidateFreq = 1
    compressedStringIndex = 0

    # When we hit the last char of the string or the next char is different
    for i in range(1, len(string)):
        s = string[i]
        if s != candidate:
            item = candidate + str(candidateFreq)
            compressedString.append(item)
            compressedStringIndex += len(item)
            candidateFreq = 1
            candidate = s
        else:
            candidateFreq += 1

    item = candidate + str(candidateFreq)
    compressedString.append(item)
    compressedStringIndex += len(item)

    compressedString = "".join(compressedString)

    if len(compressedString) >= len(string):
        return string
    else:
        return compressedString
        

t1 = time.time()
assert compress("aabcccccaaa") == "a2b1c5a3"
assert compress("abcd") == "abcd"
assert compress("aaaaaabcd") == "a6b1c1d1"
t2 = time.time()
print(t2 - t1)

t1 = time.time()
assert compressv2("aabcccccaaa") == "a2b1c5a3"
assert compressv2("abcd") == "abcd"
assert compressv2("aaaaaabcd") == "a6b1c1d1"
t2 = time.time()
print(t2 - t1)