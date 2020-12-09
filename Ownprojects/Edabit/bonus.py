def bonus(days):
    totalBonus = 0
    for day in range(1, days+1):
        if 33 <= day <= 40:
            totalBonus += 325
        elif 41 <= day <= 48:
            totalBonus += 550
        elif day > 48:
            totalBonus += 600
    return totalBonus


print(bonus(15))
print(bonus(37))
print(bonus(50))
