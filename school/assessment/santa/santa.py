import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
import tkinter
# from PIL import Image
# from PIL import ImageTk

def naughtyNice(listForPrediction):
    data = pd.read_csv("database.csv", sep=',')

    data = data[["age", "sex", "goodDeeds", "badDeeds", "status"]]

    predict = "status"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    best = 0

    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

        linear = linear_model.LinearRegression()
        linear.fit(x_train, y_train)

        acc = linear.score(x_test, y_test)

        if acc > best:
            best = acc
            print(best)
            with open("model.pickle", "wb") as f:
                pickle.dump(linear, f)

    pickle_in = open("model.pickle", "rb")
    linear = pickle.load(pickle_in)

    print(x_test)
    prediction = np.array(listForPrediction)
    print(linear.predict(prediction))
    return linear.predict(prediction)

    # p = 'age'
    # style.use("ggplot")
    # pyplot.scatter(data[p], data[predict])
    # pyplot.xlabel(p)
    # pyplot.ylabel("Status")
    # pyplot.show()



listForPrediction = []
questions = ["How old are you?",
"What is your sex?(1 for male, 0 for female)",
"How many good deeds have you done? (max 50)",
"How many bad deeds have you done? (max 50)"]
# ============== tkinter ==============

count = 0
def enter_pressed(event):
    global count
    try:
        temp = int(inputBox.get())
        count += 1
        questionText.set("Are you naughty or nice?")
    except ValueError:  # catches errors like using letters or box left blank
        questionText.set("Invalid input")

    inputBox.delete(0, 'end')  # clears input box
    listForPrediction.append(temp)

    try:
        inputValue.set(questions[count])
    except IndexError:
        try:
            print(listForPrediction)
            predict = naughtyNice([listForPrediction])
            if predict >= [0.5]:
                questionText.set("Nice!")
            else:
                questionText.set("Naughty >:(")
        except ValueError:
            questionText.set("Invalid inputs, try to restart")




mainWindow = tkinter.Tk()  # creates tkinter object

mainWindow.bind('<Return>', enter_pressed)

mainWindow.title("Santa's grotto!")
mainWindow.geometry('640x480+8+400')


# configure grid for the widgets
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)

mainWindow.rowconfigure(0, weight=2)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=1)

# image2 =Image.open('image.jpg')
# image1 = ImageTk.PhotoImage(image2)
# label1 = tkinter.Label(mainWindow, image=image1, fg="blue")
# label1.place(x=0, y=0, relwidth=1, relheight=1)


# first header
header = tkinter.Label(mainWindow, text="Santa's grotto!")
header.config(font=("Courier", 40))
header.grid(row=0, column=1, sticky='nsew')

# second header
questionText = tkinter.Variable(mainWindow)
questionText.set("Are you naughty or nice?")
questionLabel = tkinter.Label(mainWindow, textvariable=questionText)
questionLabel.config(font=("Courier", 30))
questionLabel.grid(row=1, column=1, sticky='nsew')

# questions header
inputValue = tkinter.Variable(mainWindow)
inputValue.set("How old are you")
inputLabel = tkinter.Label(mainWindow, textvariable=inputValue)
inputLabel.config(font=("Courier", 12))
inputLabel.grid(row=2, column=1, sticky='n')

# input box
inputBox = tkinter.Entry(mainWindow, justify='center')
inputBox.config(font=("Courier", 20))
inputBox.grid(row=2, column=1)

# starts the mainloop
mainWindow.mainloop()
