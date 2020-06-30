iterator = int(input('How many numbers would you like to average? :'))
total = 0
for i in range(1,iterator+1):
    num = int(input('Add a number:'))
    total += num
mean = total / iterator
print(mean)
