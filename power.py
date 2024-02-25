import pandas as pd

df=pd.read_csv("power.csv")
df=df.drop(['ts'],axis=1)
df=df[['irr','tamb','tmodule','wind','pack']]
print(df.info())

#