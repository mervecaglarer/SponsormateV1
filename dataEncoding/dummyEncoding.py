#we can also use get_dummies
import pandas as pd

data=pd.read_csv("dirtyData.csv", sep=';')

pd.get_dummies(data,columns=["province"]).to_csv('encoded.csv', index=False)