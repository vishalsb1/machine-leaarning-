import pandas as pd 

data=pd.read_csv('data.csv')
# print(type(data['Temperature']))
data_dict=data.to_dict()

# print(data_dict)

# challenge 1 
average_temp=sum(data['Temperature'])/len(data['Temperature'])
print(average_temp)
# or
print(data['Temperature'].mean())

# 2
print(data['Temperature'].max())

# 3
print(data[data.Temperature== data.Temperature.max()])