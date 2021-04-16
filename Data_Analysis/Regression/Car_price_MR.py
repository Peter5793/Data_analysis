# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Sun Jan  3 20:13:31 2021

@author: Peter Lugalia

"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import the dataset for the car price
car_df = pd.read_csv('C:/Users/hp/Desktop/Data Excerise/CarPrice_Assignment - CarPrice_Assignment.csv')
car_df.head()
# check for missing vlaues in the data set
car_df.apply(lambda x: sum(x.isnull()), axis = 0)
#check for correaltion in between the variables
car_df_corr = car_df.corr()
#display the correlation 
plt.figure(figsize=(10,9))
sns.heatmap(car_df_corr, annot = True)
plt.title('Correlation between the variables')
#exploration and analysis of the data
#divide the data into attributes and labels
x = car_df.iloc[:,:-1].values
y = car_df.iloc[:, [14]].values

#import the sklearn to split the data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size = 0.3, random_state = 0)

#fitting the model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)                                                    
#making the prediction 
y_pred = regressor.predict(x_test)
# getting the intercept and the co-effiecient
a = regressor.intercept_
b = regressor.coef_
print(a)
print('==================================')
print(b)
print('Intercept{},co-effiecient{}'.format(a, b))
