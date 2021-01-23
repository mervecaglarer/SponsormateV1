import category_encoders as ce
import pandas as pd

data=pd.read_csv("dirtyData.csv", sep=';')

encoder=ce.OneHotEncoder(cols='province',handle_unknown='return_nan',return_df=True,use_cat_names=True)
data_encoded = encoder.fit_transform(data).to_csv('encode_province.csv', index=False)

data2=pd.read_csv("encode_province.csv", sep=',')

encoder=ce.OneHotEncoder(cols='sector',handle_unknown='return_nan',return_df=True,use_cat_names=True)
data_encoded = encoder.fit_transform(data2).to_csv('encode_province_sector.csv', index=False)

data3=pd.read_csv("encode_province_sector.csv", sep=',')

encoder=ce.OneHotEncoder(cols='type',handle_unknown='return_nan',return_df=True,use_cat_names=True)
data_encoded = encoder.fit_transform(data3).to_csv('encode_province_sector_type.csv', index=False)

data4=pd.read_csv("encode_province_sector_type.csv", sep=',')

encoder=ce.OneHotEncoder(cols='scope', handle_unknown='return_nan', return_df=True, use_cat_names=True)
data_encoded = encoder.fit_transform(data4).to_csv('encoded_data.csv', index=False)