'''
Write a function to Merge 2 sorted lists in an ascending order. The func-
tion parameters are the 2 lists. The function should return the resultant
sorted list. You should test the below examples and check that the output
for each time is the same:
1
Prolbem 2
'''

def mergeSort(list1, list2):
    
    #Variables for logic
    sizeOfSortedList = len(list1) + len(list2)
    numberOfIterations = 0
    sortedList = []
    locationAtL1 = 0
    locationAtL2 = 0

    #Runs until the numberOfIterations and sizeOfSortedList are equal
    while numberOfIterations < sizeOfSortedList:

        #Checks to make sure that the location isn't larger the the length of the origional list and comapring values of the lists 
        if locationAtL1 < len(list1) and (locationAtL2 >= len(list2) or list1[locationAtL1] <= list2[locationAtL2]):

            #Adds the value to the sorted listm and increments the location
            sortedList.append(list1[locationAtL1])
            locationAtL1 += 1

        else:

            #Adds the value to the sorted list and increments the location
            sortedList.append(list2[locationAtL2])
            locationAtL2 += 1

        #Updates the numberOfIterations so there is not an index out of bounds error
        numberOfIterations += 1

    #Prints the new sortedList
    print(sortedList)

    retu


mergeSort([1, 3, 5, 7], [2, 4, 6, 8])
mergeSort([0, 7, 9, 12], [0, 1, 2, 3, 4, 7, 12])