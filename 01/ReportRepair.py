# checks if number one plus number two equals 2020
def checkNumbers(firstNumber, secNumber):
    if firstNumber + secNumber == 2020:
        return True
    return False


numbers = open("input.txt")
numberList = []
for number in numbers:
    numberList.append(int(number.rstrip()))

finished = False

# iterate through all different number combinations in the List
for firstNumber in numberList:
    for secNumber in numberList:
        if checkNumbers(firstNumber, secNumber) and not finished:
            print(f"{firstNumber} + {secNumber} = 2020")
            print(f"{firstNumber} * {secNumber} = " + str(firstNumber * secNumber))
            finished = True
