# The standard library is the module library that comes with python without having to import it,
# like the print() function

print(dir())

# When a file / function starts with an underscore, it means that it shouldn't be changed under most circumstances

# for m in dir(__builtins__):
#     print(m)

# __builtins__ states all the built in function in python that do not have to be imported to be used

# =========================

import shelve
# print(dir())
# print()
# print(dir(shelve))

# =========================

# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)

# help(shelve)

import random
help(random.randint)