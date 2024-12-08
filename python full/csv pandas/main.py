
# method 1
# data=[]
# with open('data.csv',mode='r') as file:
#     a=file.readlines()
#     for i in a:
#         data.append(i)
import csv
with open('data.csv',mode='r')as file:
    data=csv.reader(file)
    temprature=[]
    for rows in data:
        if rows[1]!="Temperature":
            number=rows[1]
            temprature.append((int(number.strip())))

print(temprature)