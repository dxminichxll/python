entries = []

if entries:
    print("all: {}".format(all(entries)))
else:
    print(False)
print("any: {}".format(any(entries)))
