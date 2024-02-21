def frequenciesOfCharacters(string):

    frequencyOfCharacters = dict()

    for char in string:

        if char in frequencyOfCharacters:

            frequencyOfCharacters[char] += 1

        else:

            frequencyOfCharacters[char] = 1

    return frequencyOfCharacters

listOfCharacters = ['abcdefg', 'hello world']

for strings in listOfCharacters:
    
    print(frequenciesOfCharacters(strings))