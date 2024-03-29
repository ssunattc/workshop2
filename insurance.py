import pandas as pd

# อ่านไฟล์
df=pd.read_csv("insurance.csv")

print(df.info())

print(df['sex'].unique())

sex_map={
    'female':0,
    'male':1,
}
df['sex']=df['sex'].map(sex_map)
print(df.head())

smoker_map={
    'yes':1,
    'no':0,
}
df['smoker']=df['smoker'].map(smoker_map)

region_encoded=pd.get_dummies(df['region'],columns=['region'],dtype=int)
print(region_encoded.head())
df=pd.concat([df,region_encoded],axis=1)
df=df.drop(['region'],axis=1)

print(df.head())

df.to_csv('ready_insurance.csv',index=False)