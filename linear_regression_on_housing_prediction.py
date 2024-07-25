# -*- coding: utf-8 -*-
"""Linear_Regression_On_Housing_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j0GG_FNquOEkz3PQREOb7qZ9fv354uh5
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv('BostonHousing.csv')
data.info()
data.shape
data.head()
da= data.isna().sum()
print(da)
X= data.drop('medv', axis=1)
y= data['medv']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
predictor = LinearRegression()
predictor.fit(X_train, y_train)
y_pred = predictor.predict(X_test)
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
# Added the import statement for matplotlib.pyplot
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))  # Adjust figure size for better visualization
plt.scatter(y_test, y_pred, color='blue', alpha=0.7, label='Data Points')  # Customize points
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2, label='Perfect Prediction')  # Add a line for perfect prediction
plt.xlabel("Actual Prices", fontsize=14)  # Increase font size
plt.ylabel("Predicted Prices", fontsize=14)
plt.title("Actual vs Predicted Housing Prices", fontsize=16)
plt.legend(loc='upper left', fontsize=12)  # Add a legend
plt.grid(True)  # Add grid for better readability
plt.show()
location = ({
    'crim': [0.05],
    'zn': [15.0],
    'indus': [2.0],
    'chas': [0],
    'nox': [0.6],
    'rm': [6.0],
    'age': [70.0],
    'dis': [4.0],
    'rad': [1],
    'tax': [296.0],
    'ptratio': [18.0],
    'b': [396.9],
'lstat': [5.0]
})
location_df = pd.DataFrame(location)
print("Predications for the new data :",predictor.predict(location_df))