'''
Practice 1
Write a program to ask the user to enter an integer and while that
integer is negative, print an error message and ask for another integer

endOfProgrom = False

number = int(input("Please enter an integer: "))

while(endOfProgrom != True):

    if (number > 0):

        print("Number is positive")
        endOfProgrom = True

    else:

        number = int(input("Number is not positive, enter another number: "))


'''

'''
Practice 2
Write a program to ask the user to enter a secret password. As long
as they don’t enter scuba, tell them that they did not enter the
correct password and ask for the password again. Once they enter the
correct password, tell them that they can come to the party
'''

setinalValue = "scuba"
correctValue = False
secretPassword = input("Please enter a password: ")

while correctValue != True:

    if secretPassword == setinalValue:

        print("Correct password entered!!")
        correctValue = True

    else:

        secretPassword = str(input("Wrong password entered. Please try again: "))





