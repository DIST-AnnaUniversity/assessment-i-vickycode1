import pandas as pd 
df = pd.read_csv("iris.csv")
avg = df["pw"].mean()
print(avg)
print(round(avg,2))
