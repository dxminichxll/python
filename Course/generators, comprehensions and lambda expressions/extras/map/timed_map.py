import timeit
text = "what have the romans ever done for us"

def char_comp():
    capitals = [char.upper() for char in text]
    return capitals

# use map
def char_map():
    map_capitals = list(map(str.upper, text))
    return map_capitals

def word_comp():
    words = [word.upper() for word in text.split(' ')]
    return words

# use map
def word_map():
    map_words = list(map(str.upper, text.split(' ')))
    return map_words

if __name__ == "__main__":

    result1 = timeit.timeit(char_comp, number=10000)
    result2 = timeit.timeit(char_map, number=10000)
    result3 = timeit.timeit(word_comp, number=10000)
    result4 = timeit.timeit(word_map, number=10000)

    print("character comprehension: {}".format(result1))
    print("character map: {}".format(result2))
    print("word comprehension: {}".format(result3))
    print("word map: {}".format(result4))
