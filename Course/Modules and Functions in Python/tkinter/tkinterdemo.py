try:
    import tkinter
except ImportError:
    import tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')
# This is resolution however we can use + to specify the position on the screen.
# In this, it is 8 pixels right and 400 pixels up

label = tkinter.Label(mainWindow, text="Hello World!")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth='1')
# canvas.pack(side='left', fill=tkinter.Y)
# canvas.pack(side='left', fill=tkinter.X, expand=True)

# canvas.pack(side='top', fill=tkinter.X, expand=True)

# canvas.pack(side='top', fill=tkinter.Y)
# canvas.pack(side='top', fill=tkinter.Y, expand=True)

# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')
#
# button1.pack(side='top', anchor='n')
# button2.pack(side='top', anchor='s')
# button3.pack(side='top', anchor='e')
# You cannot anchor north or south if the button is packed to the top, as demonstrated above
# n = north, s = south

mainWindow.mainloop()
