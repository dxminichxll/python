num = int(input('Pick a number:'))
initalNum = num
num2 = 0
loop = 0

while num != 1 and loop != 1000:
    for i in str(num):
        i = int(i)**2
        num2 += i
    num = num2
    num2 = 0
    loop += 1

if loop == 1000:
    print(initalNum, "is not a happy number")
else:
    print(initalNum, "is a happy number")

