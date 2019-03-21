# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:20:39 2018

@author: Kristi
"""

#develop a classification model based on the training set and use that model to make predictions for the test set

#import packages and pandas
import pandas as pd

import keras

#import training and testing data
#Each row in the train and test sets represent a 28 by 28 image.
train_data = pd.read_csv("C:/Users\Kristi/Documents/Fall 2018/STAT 441/DataChallenge 1/fashion-mnist_train.csv")
test_data = pd.read_csv("C:/Users\Kristi/Documents/Fall 2018/STAT 441/DataChallenge 1/test_data.csv")
train_data.head() #60000 rows × 785 columns

#split training into input and output
X = train_data.iloc[:,1:785] 
Y = train_data.iloc[:,0] #labels
print(train_data.shape, X.shape, Y.shape)



#Create model
model = Sequential()
model.add(Dense(8, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(6, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))



#make predictions for the test set
label_pred = classifier.predict(Xtestdata)

#print sumbmission results to a csv 
submission = pd.DataFrame(label_pred, columns=["label"])
submission.head()
submission.to_csv("C:/Users\Kristi/Documents/Fall 2018/STAT 441/DataChallenge 1/submission.csv")