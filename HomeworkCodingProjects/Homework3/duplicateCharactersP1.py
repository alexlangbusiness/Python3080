'''
Using a dictionary, Find all duplicate characters in a string (ignore the
case sensitive). Otherwise, print nothing.
P1
'''

duplicateCharacters = dict()

stringOfCharacters = input("Please enter a string ")
stringOfCharacters = stringOfCharacters.lower()

for character in stringOfCharacters:

    if character.isalpha():

        duplicateCharacters[character] = duplicateCharacters.get(character, 0) + 1

for char, count in duplicateCharacters.items():

    if count > 1:

        print(f"{char}", end=' ')
