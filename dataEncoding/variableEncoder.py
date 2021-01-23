import numpy as np #for numpy operations
import pandas as pd #for creating DataFrame using Pandas
import csv

data = pd.read_csv('dirtyData.csv')

forOneHotSome = data[['province','type','scope']]
forOneHotSome = pd.get_dummies(forOneHotSome)

forOneHotFull = data[['province','type','sector','scope']]
forOneHotFull = pd.get_dummies(forOneHotFull)

del data['type']
del data['scope']
del data['province']

# create the dictionary
count_map_sector = data['sector'].value_counts().to_dict()
total = sum(count_map_sector.values())
for key,value in count_map_sector.items():
  count_map_sector[key] = value / total * 100

data['sector'] = data['sector'].map(count_map_sector)

encoded_data_1 = data.join(forOneHotSome)

del data['sector']

encoded_data_2 = data.join(forOneHotFull)
encoded_data_1.to_csv('data.csv', index=False,encoding='utf-8')
encoded_data_2.to_csv('data.csv', index=False,encoding='utf-8')

