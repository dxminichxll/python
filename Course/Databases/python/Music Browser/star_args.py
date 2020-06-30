# def average(*args):
#     print(type(args))
#     print("args is {}:".format(args))
#     print("*args is:", *args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
# *args unpacks the tuple args
#
# print(average(1, 2, 3, 4))


# def build_tuple(*args):
#     return args
#
#
# message_tuple = build_tuple("Hello", "planet", "earth", "take", "me", "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)
#
# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)


# def print_backwards(*args, end=' ', **kwargs):
#     # If you want to override the users input, you can include the named parameter in the function,
#     # so it is not passed to **kwargs
#     # def print_backwards(*args, **kwargs):
#     print(kwargs)
#     # kwargs.pop('end', None)
#     # Kwargs is a dictionary and ** unpacks the dictionary
#     # Kwargs.pop takes 'end' out of the dictionary if it is there
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

# def print_backwards(*args, end=' ', **kwargs):
#     end_character = kwargs.pop('end', '\n')
#     sep_character = kwargs.pop('sep', ' ')
#     for word in args[:0:-1]:
#         print(word[::-1], end=sep_character, **kwargs)
#     print(args[0][::-1], end=end_character, **kwargs)
#     # print(end=end_character)


def print_backwards(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")

# print()
# print("Hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
# print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep=' ')

