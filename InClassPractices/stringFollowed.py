'''
Write a Python program that matches a string that has an a followed
by zero or more b’s
'''

import re

def checkPattern(pattern, strings):

    return bool(re.match(pattern, strings))

pattern = "^a(b*)$"
strings = ["a", "ab", "abc", "afs", "abg", "asba"]

for string in strings:

    print(checkPattern(pattern, string))

