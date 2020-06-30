print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number to square it: "))

squares = [number ** 2 for number in numbers]
# ^^ the loop control variable is not modified throughout the program
# Unlike in listfor.py, we can have the use the variable 'number'
# inside the loop as well as outside the loop

# squares = [number ** 2 for number in range(1, 7)]

print(squares)

index_pos = numbers.index(number)
print(squares[index_pos])