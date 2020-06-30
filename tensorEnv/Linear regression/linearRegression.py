import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

# https://www.youtube.com/watch?v=1BYu65vLKdA&list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr&index=3
# ^^ Link to explanation of linear regression

data = pd.read_csv("student-mat.csv", sep=';')
# ^^ loads the data set into the python project

# print(data.head())
# ^^ prints the first 5 values in the dataset

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
# ^^ selects only a few attributes that we will be using
# print(data.head())

predict = "G3"
# ^^ This is also known as a label. It is the attribute we are trying to predict

X = np.array(data.drop([predict], 1))
# ^^ this creates an array without our label, which is the value we are trying to calculate
y = np.array(data[predict])
# ^^ this creates an array of just our label

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

"""
best = 0
# ^^ Keeps track of the best accuracy so far
for _ in range(30):
    # The training process is repeated and the best accuracy is kept

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
    # This splits all of our data. It takes 10% of the data so we can use it for training purposes

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    # This creates a line of best fit using the x_train and y_train data to train it.

    acc = linear.score(x_test, y_test)
    # ^^ this tests our line of best fit against some data, and it will provide an accuracy of the program
    print(acc)

    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
"""

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

print("Co: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = 'G1'

style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.xlabel("Final grade")
pyplot.show()