def initialise():
    global total, n
    print("This program finds the maximums of sets of three numbers. Enter three zeroes when all numbers entered. Program then calculates and outputs the average of the maximums")
    total = 0
    n = 0

def promptForNumbers():
    num1 = int(input("Please enter first number "))
    num2 = int(input("Please enter second number "))
    num3 = int(input("Please enter third number "))
    
    return num1, num2, num3

def findMax(num1, num2, num3):
    maxnum = num1
    if num2>maxnum:
        maxnum = num2
    if num3>maxnum:
        maxnum = num3
    print("Max of the three numbers is is ",maxnum)
    return maxnum

def performCalculations(maxnum):
    global total, n
    total += maxnum
    n+=1

def processData():
    global total, n
    num1, num2, num3 = promptForNumbers()
    while num1!=0 or num2 != 0 or num3 != 0:
        maxnum = findMax(num1, num2, num3)
        performCalculations(maxnum)
        num1, num2, num3 = promptForNumbers()

def calculateAverage():
    global total, n
    average = total/n
    print("Average of maximums is", average)

total = 0
n = 0
initialise()
processData()
calculateAverage()
