# Given a string and its true length, replace all spaces with %20.
# Do this in place (don't create a new string)
# Example:
#   Input: "Mr John Smith    ", 13
#   Output: Mr%20John%20Smith"

import time

# Count number of whitespaces in range.
def URLify(string, trueLength):
    index = len(string)

    for i in range(trueLength - 1, -1, -1):
        if string[i] == " ":
            index -= 3
            string[index:index + 3] = "%20"
        else:
            index -= 1
            string[index] = string[i]
    return "".join(string)
            



# test = "Mr John Smith    "
test = list("much ado about nothing      ")

print(URLify(test, 22))