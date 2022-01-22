#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pickle
import numpy as np
import sys







# In[12]:


filename="Loan_Prediction_Model"
loaded_model=pickle.load(open(filename,'rb'))



Gender = sys.argv[1]
Marital_Status = sys.argv[2]
No_of_Dependents = int(sys.argv[3])
Education = sys.argv[4]
Self_Employed = sys.argv[5]
Income = int(sys.argv[6])
Coapplicant_Income = int(sys.argv[7]) 
Loan_Amount = int(sys.argv[8])
Loan_Amount_Term = int(sys.argv[9])
Credit_History = int(sys.argv[10])
Property_Location = sys.argv[11]


if Gender=='Male':
    Gender = 1
else:
    Gender = 0

if Marital_Status=='Married':
    Marital_Status = 1
else:
    Marital_Status = 0

if No_of_Dependents>=2:
    No_of_Dependents = 4
else:
    No_of_Dependents = No_of_Dependents

if Education=='Graduate':
    Education = 1
else:
    Education = 0

if Self_Employed=='Yes':
    Self_Employed = 1
else:
    Self_Employed = 0

if Property_Location=='Rural':
    Property_Location = 0
elif Property_Location=='Semiurban':
    Property_Location = 1
else:
    Property_Location = 2

Gender = int(Gender)
Marital_Status = int(Marital_Status)
Education = int(Education)
Self_Employed = int(Self_Employed)
Property_Location = int(Property_Location)

input_data = [Gender,Marital_Status,No_of_Dependents,Education,Self_Employed,Income,Coapplicant_Income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Location]

#changing input data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape tghe array as we are predicting only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#standardize the input data
#std_data = scaler.transform(input_data_reshaped)

prediction=loaded_model.predict(input_data_reshaped)

if (prediction[0] == 0):
    print("Loan Not Approved")
else:
    print("Loan Approved")

