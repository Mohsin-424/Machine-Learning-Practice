# Importing Libraries

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Loading the dataset
data = pd.read_csv('Salary_Data.csv')
X = data.iloc[:,:-1].values # X is predictor
y = data.iloc[:,-1].values # Y is response

# Split dataset into test and training set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

# Training Linear Regression Model

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting test set results

y_predicted = regressor.predict(X_test)
print(y_predicted)

# Visualizing the Training set results

plt.scatter(X_train, y_train, color='red')
alpha = regressor.predict(X_train)
plt.plot(X_train, alpha, color='#00FF00')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the Test set results
plt.scatter(X_test, y_test, color='blue')
alpha = regressor.predict(X_train)
plt.plot(X_train, alpha, color='#000000')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()