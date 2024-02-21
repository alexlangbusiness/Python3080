'''
Write a program that has a function that accepts 3 parameters.
▶ Each parameter represents a side of the three sides of a triangle.
▶ The function returns the largest side.
▶ If the three sides could not possibly make a triangle, return ”Not a
Triangle”. How do we determine if a triangle is valid based on its 3
sides? the sum of two side lengths of a triangle is always greater than
the third side
'''

import math

def findLargestSide(size1, size2, size3):

    largestSize =0

    if (largestSize <= size1):
        largestSize = size1
    
    if (largestSize <= size2):
        largestSize = size2
    
    if (largestSize <= size3):
        largestSize = size3

    if (size1 + size2 <= size3 or size2 + size3 <= size1 or size1 + size3 <= size2):
        print("Not a triangle ")

    else:
        print(largestSize)


findLargestSide(4, 7, 5)
findLargestSide(4, 9, 4)

2
