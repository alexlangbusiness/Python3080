'''
Write a function to check if the list contains at least one of three consec-
utive common numbers. The function parameter is a list. The function
should return a boolean value. You should test the below examples and
check that the output for each time is the same:
Question1
'''

#Function header
def findConsecutiveNumbers(listOfNumbers):

    #Variable that keeps track of how many numbers in a row are equal to each other
    currentInARow = 0

    #Runs for the entire list of numbers unless 3 in a row are found, but then true is returned 
    for i in range(1, len(listOfNumbers)):

        #Checks to see if the values are equal
        if listOfNumbers[i] == listOfNumbers[i - 1]:

            #Increments by 1 if they are equal
            currentInARow += 1

        else:

            #Resets the number of values in a row if not equal
            currentInARow = 0
        
        #Returns true if 3 values in a row are true
        if currentInARow >= 2:

            return True
    
    return False

#Tests the function with 3 diffrent lists
print(findConsecutiveNumbers([-4, 9, 9, 9, 3, 8]))
print(findConsecutiveNumbers([5, 3, 3, 7, 7, -2, -2]))
print(findConsecutiveNumbers([12, 12, 12, 12, 5, 5, 2, 2]))
