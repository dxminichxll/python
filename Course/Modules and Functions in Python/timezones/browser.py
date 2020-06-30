import webbrowser

# webbrowser.open("https://www.python.org/")
# help(webbrowser)
#
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, sep=';', end=' ')
#     # The print function takes many arguments like 'sep' where you can classify a separator (default is space)
#     # It also takes an 'end' argument which determines what is at the end of a string (default is new line)
#

# webbrowser.open("https://www.python.org/", new=2)
# # The new parameter only works 'if possible' so it won't work with my browser

chrome = webbrowser.get(using='windows-default')
chrome.open_new("https://www.python.org/")
# The 'using' parameter takes a browser