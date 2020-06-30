import webbrowser

website = input('enter a website name')
website = 'http://www.' + website + '.com'
for i in range(2):
    webbrowser.open(website)

# while True:
#     webbrowser.open(website)
