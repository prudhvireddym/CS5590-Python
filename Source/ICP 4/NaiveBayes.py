# Required Imports
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plot
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Loading Iris datasets
iris = datasets.load_iris()

# Fitting Naive Bayes model to the data
model = GaussianNB()
model.fit(iris.data, iris.target)
print(model)

# Making Prediction based on X, Y
expected = iris.target
predicted = model.predict(iris.data)
print(expected,":", predicted)
# Matlib Plot
plot.plot(expected, predicted)
plot.show()

# Cross Validation

print(metrics.classification_report(expected, predicted))
# confusion_matrix - To evaluate Accuracy of classification
print(metrics.confusion_matrix(expected, predicted))

# splitting data and target into training and testing sets
"""http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html"""
# If int, random_state is the seed used by the random number generator
# If float, test_size represent the proportion of the dataset to include in the test split [Default: 0.25]
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=1)

# Training the Model on Training Set
model.fit(X_train, Y_train)

# Training the Model on Testing Set
Y_predicted = model.predict(X_test)

# Evaluating the Model based on Testing Part
print("Gaussian Model Accuracy is ", metrics.accuracy_score(Y_test, Y_predicted) * 100)
