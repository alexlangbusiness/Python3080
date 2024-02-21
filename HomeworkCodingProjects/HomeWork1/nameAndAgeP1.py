'''
Write a program to ask for the name and the age. Then, print the name
5 times (do not use loops), and the age after 5 years.
Prolbem #1
'''

#Asks user for thier name and age, saves those values in variables
name = str(input("Please, enter your name: "))
age = int(input("Please, enter your age: "))

#Just prints out the name 5 times, specified to not use a loop
print("Your name (repeated 5 times): " + name + " " + name + " " + name + " " + name + " " + name)

#Increments age by 5
age += 5

#Prints updated age
print("Your age after 5 years: " + str(age))