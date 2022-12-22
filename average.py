import pandas as pd
df = pd.read_csv("iris.csv")
avg = df["pw"].mean()
print(avg)
print(round(avg,2))

#read csv file
#find the average of petal width
#round off to 2 decimal places
#print only average
