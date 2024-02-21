'''
Print dogs’ names alphabetically ordered by their names.
Determine if there is an aussie shepherd.
Print the dog details of aussie shepherd.
Print the oldest dog details.
Use a dictionary comprehension to pull out all the dogs 8 or older.
'''

import sys

dogs = {'Brodie': {'age': 4, 'breed': 'border collie'}, 
        'Scruffy': {'age' : 8, 'breed': 'border collie'},
        'Zoey': {'age': 12, 'breed' : 'aussie shepard'},
        'Lexie': {'age': 6, 'breed' : 'labrador retriever'}
    }

dogsNames = list(dogs.keys())
dogsNames.sort()
print(dogsNames)

for keys in dogs.keys():

    if 'aussie shepard' in dogs[keys].values():

        print("Yes there is an aussie shepard")

for keys in dogs.keys():

    if dogs[keys]['breed'] == 'aussie shepard':

        print(keys, " ", dogs[keys])
        break

oldestAge = -sys.maxsize
oldestAgeKey = None
oldestAgeValue = None

for key in dogs.keys():

    if dogs[key]['age'] > oldestAge:
        
        oldestAge = dogs[key]['age']
        oldestAgeKey = key
        oldestAgeValue = dogs[key]

print("Oldest Age:", oldestAge)
print("Dog Key:", oldestAgeKey)
print("Dog Value:", oldestAgeValue)

dogsOlderThanEight = {key: dogs[key] for key in dogs.keys() if dogs[key]['age'] >= 8}
print(dogsOlderThanEight)