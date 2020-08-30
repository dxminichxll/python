entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("Iterable with a 'false' value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print('='*40)

# python recognises empty values as false.
# bool(0) = False as well as many other things like empty strings and tuples


name = ""
if name:
    print("Hello {}".format(name))
else:
    print("welcome, person with no name")
