import random
import time

functionList = ["*", "/", "+", "-"]
points = 0

print("Welcome to the quiz, here's the rules:")
time.sleep(2)
print("You will be asked a question, and you answer it")
time.sleep(2)
print("If you are correct, you gain 1 point, if you are incorrect, you lose 1 point\n")
print('=' * 40)

time.sleep(2)

questionNum = 0

while True:

    if questionNum < 21:

        print("Points", points)
        print("Question", questionNum, "/ 20")
        number1 = random.randint(1,20)
        number2 = random.randint(1,20)
        function = random.choice(functionList)


        if function == "*":
            answer = number1 * number2

        elif function == "/":
            if number1 % number2 == 0:
                answer = number1 / number2
            else:
                answer = number1 * number2
                function = "*"

        elif function == "+":
            answer = number1 + number2
        elif function == "-":
            answer = number1 - number2


        print(number1, function, number2)
        userAns = float(input("Answer:"))

        if userAns == answer:
            print("You are correct")
            print('=' * 40)
            points += 1
            questionNum += 1
        else:
            print("That is incorrect, the answer was", answer)
            print('='*40)
            points -= 1
            questionNum += 1

    else:
        print("The quiz is over, you scored {} out of 20".format(points))
        break