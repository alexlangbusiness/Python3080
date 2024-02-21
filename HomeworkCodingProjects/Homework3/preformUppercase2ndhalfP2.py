'''
Write a Python program to perform uppercase of the second half of a
given string.
P2
'''

fullString = input("Please enter a string: ")

sizeOfString = len(fullString)

if sizeOfString % 2 == 0:

    start_index = sizeOfString // 2

else:

    start_index = sizeOfString // 2 + 1

second_half_uppercase = fullString[:start_index] + fullString[start_index:].upper()

print(second_half_uppercase)
