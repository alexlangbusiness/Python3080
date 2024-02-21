'''
Write a Python program to accept a positive integer number from the user
and print the following pattern using loops.
Prolbem #3
'''

#Gets number of n that will determine the number of rows of asterics
number = int(input("Please, enter the value of n: "))

#Checks to see if that number is positive or not
if number >=1:

    #Nested for loop that will run number amount of times
    for i in range(number):

        #Inner nested for loop that prints a * for each value of number
        for j in range(number):

            print("* ", end ="")

        #Goes to a new line, and decremens the number of astrics by 1
        print("")
        number-=1


else:
    print("Invalid input")