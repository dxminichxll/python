menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# ^^ This comprehension has a "filter" which makes it conditional. The filter only allows specific values through
# You can't use an else clause because it is only a filter
# You can concatenate multiple filters
# "and" or "if" can be used to concatenate filters
print(meals)

fussy_meals = [meal for meal in menu if
               "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
# The statement in the brackets means that the meal wont be added to the list if bacon AND sausage are in the meal
# but either bacon or sausage on its own is fine.
print(fussy_meals)

fussy_meals = [meal for meal in menu if
               ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
# This does the same thing as before but it is fit into one filter
print(fussy_meals)
