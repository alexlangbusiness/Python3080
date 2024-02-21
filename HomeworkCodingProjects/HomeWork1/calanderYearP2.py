'''
Write a Python program that inputs a calendar year. Then, check whether
this is a leap year or not.
Prolbem #2
'''

#Boolean Value that keeps track if a proper leap year was entered or not
correctYearEntered = False

#While loop that runs until a correct year is entered
while correctYearEntered != True:

    #Takes a number value as a year value that will be checked if its a leap year or not
    year = int(input("Please, enter the year (in YYYY format): "))

    #Then uses mod to check to see if there is a remaineder or not
    #Then prints if it's a leap year or not
    if year % 4 != 0:

        print("This is not a leap year.")

    else:

        print("This is a leap year")
        correctYearEntered = True