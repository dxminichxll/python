# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:
    import tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('175x175-8-220')
mainWindow['padx'] = 8
mainWindow.resizable(0, 0)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)


inputBox = tkinter.Entry(mainWindow)
inputBox.grid(row=0, column=1, sticky='nw', columnspan=4)

mainFrame = tkinter.Frame(mainWindow)
mainFrame.grid(row=1, column=1, sticky='nw')


CButton = tkinter.Button(mainFrame, text="C")
CEButton = tkinter.Button(mainFrame, text="CE")
CButton.grid(row=1, column=0, sticky='nw')
CEButton.grid(row=1, column=1, sticky='nw')
CButton['padx'] = 8
CEButton['padx'] = 8

sevenButton = tkinter.Button(mainFrame, text='7')
eightButton = tkinter.Button(mainFrame, text='8')
nineButton = tkinter.Button(mainFrame, text='9')
addButton = tkinter.Button(mainFrame, text='+')
fourButton = tkinter.Button(mainFrame, text='4')
fiveButton = tkinter.Button(mainFrame, text='5')
sixButton = tkinter.Button(mainFrame, text='6')
minusButton = tkinter.Button(mainFrame, text='-')
oneButton = tkinter.Button(mainFrame, text='1')
twoButton = tkinter.Button(mainFrame, text='2')
threeButton = tkinter.Button(mainFrame, text='3')
multiplyButton = tkinter.Button(mainFrame, text='*')
zeroButton = tkinter.Button(mainFrame, text='0')
equalsButton = tkinter.Button(mainFrame, text='=')
divideButton = tkinter.Button(mainFrame, text='/')

sevenButton.grid(row=2, column=0, sticky='ew')
eightButton.grid(row=2, column=1, sticky='ew')
nineButton.grid(row=2, column=2, sticky='ew')
nineButton['padx'] = 6
addButton.grid(row=2, column=3, sticky='ew')
addButton['padx'] = 6
fourButton.grid(row=3, column=0, sticky='ew')
fiveButton.grid(row=3, column=1, sticky='ew')
sixButton.grid(row=3, column=2, sticky='ew')
minusButton.grid(row=3, column=3, sticky='ew')
oneButton.grid(row=4, column=0, sticky='ew')
twoButton.grid(row=4, column=1, sticky='ew')
threeButton.grid(row=4, column=2, sticky='ew')
multiplyButton.grid(row=4, column=3, sticky='ew')
zeroButton.grid(row=5, column=0, sticky='ew')
equalsButton.grid(row=5, column=1, sticky='ew', columnspan=2)
divideButton.grid(row=5, column=3, sticky='ew')


tkinter.mainloop()
