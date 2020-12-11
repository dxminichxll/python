import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("database.csv", sep=',')

data = data[["age", "sex", "goodDeeds", "badDeeds", "status"]]
# ^^ selects only a few attributes that we will be using

predict = "status"
# ^^ This is a label. It is the attribute we are trying to predict

X = np.array(data.drop([predict], 1))
# ^^ this creates an array without our label, which is the value we are trying to calculate
y = np.array(data[predict])
# ^^ this creates an array of just our label

best = 0
# ^^ Keeps track of the best accuracy so far
for _ in range(100):
    # The training process is repeated and the best accuracy is kept

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
    # This splits all of our data. It takes 10% of the data so we can use it for training purposes

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    # This creates a line of best fit using the x_train and y_train data to train it.

    acc = linear.score(x_test, y_test)
    # ^^ this tests our line of best fit against some data, and it will provide an accuracy of the program
    # print(acc)

    if acc > best:
        best = acc
        print(best)
        with open("model.pickle", "wb") as f:
            pickle.dump(linear, f)
        # Saves our best test to a file


pickle_in = open("model.pickle", "rb")
linear = pickle.load(pickle_in)

print(x_test)
prediction = np.array([[10, 1, 50, 50]])
print(linear.predict(prediction))

p = 'age'
style.use("ggplot")
pyplot.scatter(data[p], data[predict])
pyplot.xlabel(p)
pyplot.ylabel("Status")
pyplot.show()
