import pandas as pd
df = pd.read_csv("iris.csv")
def range():
    #calculate the range of pw#
    range_pw = df.pw.max()-df.pw.min()
    return (range_pw) 

rn = range()
print(rn)
