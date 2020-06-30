# def python_food():
#     print("Spam and eggs")8
#
#
# python_food()
# print(python_food())

# =======================================================


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text) // 2)
    print(" "*left_margin, text)


# python_food()

# =======================================================
# def centre_text(text):
#     text = str(text)
#     left_margin = (80 - len(text) // 2)
#     print(" " * left_margin, text)

# =======================================================


# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
#     # ^^ asterix means there can be a variable number of parameters
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text) // 2)
#     print(" " * left_margin, text, sep=sep, end=end, file=file, flush=flush)
#
# # Refactor can be used in pycharm to rename variables or functions (highlight and right click)
#
#
# # Print into a .txt file using the file parameter
# with open("centred", mode='w') as centred_file:
#     centre_text("Spam and eggs", file=centred_file)
#     centre_text("Spam, spam and eggs", file=centred_file)
#     centre_text(12, file=centred_file)
#     centre_text("Spam, spam, spam and eggs", file=centred_file)
#     centre_text("first", "second", 3, 4, "spam", sep=":", file=centred_file)

# =======================================================

def centre_text(*args, sep=' '):
    # ^^ astrix means there can be a variable number of parameters
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    return " " * left_margin + text


with open("menu", "w") as menu:
    s1 = centre_text("Spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("Spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("Spam, spam, spam and eggs"),file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)
