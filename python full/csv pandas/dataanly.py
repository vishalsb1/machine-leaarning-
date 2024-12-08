import pandas as pd
data=pd.read_csv('data2.csv')
gray = sum(data['Primary Fur Color']=='Gray')
print(gray) 
red = sum(data['Primary Fur Color']=='Cinnamon')
print(red) 
Black = sum(data['Primary Fur Color']=='Black')
print(Black) 