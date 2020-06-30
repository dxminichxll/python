def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

# for f in fib:
#     print(f)

for i in range(100):
    print(next(fib))