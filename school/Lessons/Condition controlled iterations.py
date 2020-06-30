#Program to add up numbers until 0 is entered
#Initialise variables
total=0
number=1
#Enter numbers to add
while number>0:
    number=int(input("Enter a number: "))
    #Add number to total
    total=total+number
#Output result
print("The sum of the numbers is:",total)


