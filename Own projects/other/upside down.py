x = 0
while x == 0:
    num = int(input("A number with only 0, 6 and 9s:"))
    for i in str(num):
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '7' or i == '8':
            if x == 0:
                print("The number must only include 0, 6 or 9s")
            x = 0
            break
        else:
            x = 1

x = str(num)
flipped = []
for i in x:
    if i == '6':
        flipped.append('9')
    elif i == '9':
        flipped.append('6')
    else:
        flipped.append('0')

flipped = ''.join(flipped)

if flipped[::-1] == x:
    print("Yes")
else:
    print("no")
