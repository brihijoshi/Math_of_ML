import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
fh = open("data/data_lr.csv","r")

x = []
y = []

for line in fh:
    try:
        tokens = line.split(",")
        x.append([float(tokens[0].strip())])
        y.append([float(tokens[1].strip())])
    except:
        continue
x = x[1:]
y = y[1:]


# Use only one feature
#diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
x_train = x[:]
x_test = x[:]

# Split the targets into training/testing sets
y_train = y[:]
y_test = y[:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x_train, y_train)
print(regr)
# Make predictions using the testing set
y_pred = regr.predict(x_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(x_test, y_test,  color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
