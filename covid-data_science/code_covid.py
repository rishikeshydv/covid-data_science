import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
file = pd.read_csv('covid_cases.csv')
#y_df = file.loc[:,'COVID_Cases']
y_df = file.drop(['Districts','Population','per_capita/PPP($)','max_temp/*C','min_temp/*C','Average age of People/years', 'No. of Hospitals'], axis = 1)
x_df = file.drop(['COVID_Cases','Districts','No. of Hospitals'], axis = 1)


X = x_df.values[:,1:]
print(X)
y = y_df.values[:]


train_X = X[:70]
train_y = y[:70]

test_X = X[70:]
test_y = y[70:]

reg = LinearRegression().fit(train_X, train_y)
#print(reg.coef_)
#print(reg.intercept_)



#test values predict
y_hat_test = reg.predict(test_X)
#print('predicted y', y_hat_test)
#print('real y', test_y)
test_mse = mean_squared_error(y_hat_test,test_y)
print('test mean squared error= ', test_mse)
test_r_squared = r2_score(y_hat_test, test_y)
print('test r^2= ', test_r_squared)


#train values predict
y_hat_train = reg.predict(train_X)
#print('predicted y', y_hat_train)
#print('real y', train_y)
train_mse = mean_squared_error(y_hat_train, train_y)
print('train mean squared error= ', train_mse)
train_r_squared = r2_score(y_hat_train, train_y)
print('test r^2= ', train_r_squared)






