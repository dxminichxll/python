import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)

print(dice1)
print(dice2)
print(dice3)


if dice1 == dice2 == dice3:
    score = dice1 + dice2 + dice3
elif dice1 == dice2:
    score = dice1 + dice2 - dice3
elif dice1 == dice3:
    score = dice1 + dice3 - dice2
elif dice2 == dice3:
    score = dice2 + dice3 - dice1
else:
    score = 0

print("Score:", score)