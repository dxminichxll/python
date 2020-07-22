plainText = input('text to order: ')
backwards = input('would you like it to be sorted in ascending or decending order? (a/d)')
ordered = [i for i in plainText]
if backwards == 'd':
    print(''.join(reversed(sorted(ordered))))
else:
    print(''.join(sorted(ordered)))
