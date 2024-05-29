# 🌟 DATA PREPROCESSING

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./pt2_regression/1_simpleLinearRegression/salary_data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=0)

# 🌟 TRAINING THE SIMPLE LINEAR REGRESSION MODEL ON THE TRAINING SET
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# 🌟 predicting the test set results
y_pred = regressor.predict(x_test)

# 🌟 VISUALISING THE TRAINING SET RESULTS
plt.scatter(x_train, y_train, color ='red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

input()

# 🌟 VISUALISING THE TEST SET RESULTS
plt.scatter(x_test, y_test, color ='red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
