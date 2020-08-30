fruit = {"orange": "a sweet or ange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citrus fruit",
        "grape": "a small sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit"
        }

# print(fruit)
# print(fruit["orange"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])
# fruit["lime"] = "great with tequila"
# print(fruit["lime"])
# del fruit["lemon"]
# print(fruit)

# =============================

print(fruit)
# while True:
#     dict_key = input("Please enter a fruit:")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a", dict_key)

    # description = fruit.get(dict_key, "We don't have a " + dict_key)
    # print(description)

# for snack in fruit:
#     print(fruit[snack])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

for val in fruit.values():
    print(val)
