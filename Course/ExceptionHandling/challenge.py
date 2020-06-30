def split(string, index):
    return int(string[index])


num1 = ""
num2 = ""
while True:
    num = input("Please enter a 2 digit number")

    if len(num) == 2:

        # num1 = int(num[0])
        # num2 = int(num[1])

        num1 = split(num, 0)
        num2 = split(num, 1)

        try:
            print(num1 / num2)
            break
        except ZeroDivisionError:
            print("You cannot divide by zero")

    else:
        pass
