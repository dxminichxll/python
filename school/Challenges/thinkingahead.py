list = []
for i in range(0, 10):
    list.append(int(input(f"enter number {i}/10: ")))
print([num for num in list if num%7==0])
