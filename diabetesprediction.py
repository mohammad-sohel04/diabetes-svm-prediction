# -*- coding: utf-8 -*-
"""DiabetesPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zg9lGiPiNuAZhLTEgG_41mqhc4j7n0xA

Importing the Dependencies
"""

import numpy as np # arrray operation
import pandas as pd # DAta frame
from sklearn.preprocessing import StandardScaler # To standerized the dataset
from sklearn.model_selection import train_test_split # to split dataset into test and trainnig
from sklearn import svm # model Support vector machine-->supervised->classification
from sklearn.metrics import accuracy_score  # to calculate the accuracy  of model

"""DAta collection and Analysis
PIMA Diabetes Dataset
"""

#loading the dataset to a Dataframe
diabetes_dataset=pd.read_csv('/content/diabetes.csv')

pd.read_csv?

#printing the first five rows  to know about dataset
diabetes_dataset.head()

# No. of rows and column
diabetes_dataset.shape

# Getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""Label 0-->Non diabetic
Label 1-->Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# separating the data and label
x=diabetes_dataset.drop(columns='Outcome',axis=1);
y=diabetes_dataset['Outcome']

#only data
print(x)

#only label
print(y)

"""Standardization of DAta"""

scaler=StandardScaler()

scaler.fit(x)

standardized_data=scaler.transform(x)

print(standardized_data)

X=standardized_data
Y=diabetes_dataset['Outcome']

print(X)
print(Y)

"""Split the data into train and Test"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2) #20 % test data

print(X.shape,X_train.shape ,X_test.shape)

"""Training the model"""

classifier=svm.SVC(kernel='linear')

#trininig the SVM classifier
classifier.fit(X_train,Y_train)

"""Model Evaluation
Accuracy Score
"""

#accuracy score from the training data
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the training data: ',training_data_accuracy)

# accuracy score of test data
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print("Accuracy of the test data :",test_data_accuracy)



"""Making a Predictive System"""

input_data=(4,110,92,0,0,37.6,0.191,30)
# convert it into numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the array as we are predicting for one instance
input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
#standardize the input data
std_data=scaler.transform(input_data_reshape)
print(std_data)

# prediction
prediction=classifier.predict(std_data)
print(prediction)
if (prediction[0])==0:
  print('The person is not diabetic')
else:
  print('The person is diabetic')

