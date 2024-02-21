myList = [10, 50, 75, 83, 98, 84, 32]

maxNumber =0

for item in myList:

    if myList[item] >= maxNumber:
        maxNumber = myList[item]

print("Output: " + maxNumber)


