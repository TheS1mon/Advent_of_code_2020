# checks if number one plus number two equals 2020
def checkNumbers(firstNumber, secNumber, thirdNumber):
    if firstNumber + secNumber + thirdNumber == 2020:
        return True
    return False


numbers = open("input.txt")
numberList = []
for number in numbers:
    numberList.append(int(number.rstrip()))

# Avoids double entrys
finished = False

# iterate through all different number combinations in the List
for firstNumber in numberList:
    for secNumber in numberList:
        for thirdNumber in numberList:
            if checkNumbers(firstNumber, secNumber, thirdNumber) and not finished:
                print(f"{firstNumber} + {secNumber} + {thirdNumber} = 2020")
                print(f"{firstNumber} * {secNumber} * {thirdNumber} = " + str(firstNumber * secNumber * thirdNumber))
                finished = True
