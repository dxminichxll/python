text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

# use map
map_capitals = list(map(str.upper, text))
print(map_capitals)

# the map function calls a function for each item in an iterable and stores the result in a new iterable
# in this case, text is the iterable and it is being iterated over each character
# each character is being passed to the str.upper function, making it upper case
# each uppercase character is then stored as a new iterable (map_capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

# use map
map_words = list(map(str.upper, text.split(' ')))
print(map_words)

for x in map(str.upper, text.split(' ')):
    print(x)
