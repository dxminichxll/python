#Get user input
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))

#Make calculations
power_of_result = number1 ** number2
division_result = number1 / number2
integer_division_result = number1 // number2
modulus_result = number1 % number2

#Output results
print()
print(number1,"to the power of",number2,"is",power_of_result)
print(number1,"divided by",number2,"is",division_result)
print(number1,"divided by",number2,"is",integer_division_result)
print(number1,"divided by",number2,"has a remainder of",modulus_result)

import random
#Roll the dice
random_number = random.randint(1,10)
print("You rolled a",random_number)

