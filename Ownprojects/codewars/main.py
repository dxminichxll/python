def generate_hashtag(s):
    result = ['#']
    if not s:
        return False
    s = s.lower()

    tempList = s.split()
    print(tempList)
    for word in tempList:
        word = list(word)
        # print(list(word)[0])
        word[0] = word[0].upper()
        word = "".join(word)
        result.append(word)
    print(result)
    result = "".join(result)
    result = result.strip()
    resultLength = len(result)
    if resultLength < 140:
        return result
    else:
        return False


# print(generate_hashtag(''))
# print(generate_hashtag('Do We have A Hashtag')[0])
# print(generate_hashtag('Codewars'))
# print(generate_hashtag('Codewars      '))
# print(generate_hashtag('Codewars Is Nice'))
# print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))
# print(generate_hashtag('c i n'))
# print(generate_hashtag('codewars  is  nice'))
# print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')
