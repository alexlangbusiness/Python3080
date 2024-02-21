'''
Write a Python program to count all the characters, except spaces.
P3
'''

message = input("Please, enter a string: ")

characterCount =0

for character in message:

    if (character != " "):
        characterCount += 1

print(characterCount)
