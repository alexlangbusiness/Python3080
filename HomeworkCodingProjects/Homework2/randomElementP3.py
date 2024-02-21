'''
Write a function to return a randomly selected element from a list. The
function parameter is the list. The function should return the randomly
selected element.
Prolbem 3
'''

#Need random import
import random as rand

#Will return a random element from a list
def randomElement(list):

    #Gets a random element from 0 and the end of list 
    randomElement = rand.randint(0, len(list)-1)

    #Gets the element from the list at the random element
    selectedNumber = list[randomElement]

    #Prints and returns the value
    print(selectedNumber)
    return selectedNumber





randomElement([5, -9, 70, 15])
randomElement([0, 1, 2, 3, 4, 7, 12])