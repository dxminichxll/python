# 2 types of errors:
# Syntax errors - errors in syntax e.g a missing colon
# Exceptions - errors in code e.g file not found

# An exception that is not handled is called an unhandled exception, and will produce an error

def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n-1)


try:
    print(factorial(1000))
except RecursionError:
    # ^^ you can specify the error name or you cannot state the error name and it will handle any error
    print("This program cannot calculate factorials at large")
except ZeroDivisionError:
    # Add another exception for a different error
    print("You absolute imbecile, what are you doing dividing by zero?")


except (RecursionError, ZeroDivisionError):
    # You can also specify 2 or more exception names by putting them in brackets
    print("This program cannot calculate factorials at large")
    # Not efficient always because this will print the same output for each error


print("Program terminating")
