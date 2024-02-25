import pandas as pd

# อ่านไฟล์
df=pd.read_csv("50_Startups.csv")

print(df.describe())

states_df=df.groupby('State')
for state,states_df in states_df:
    print(state)
    print(states_df.describe())

import matplotlib.pyplot as plt
cols=['R&D Spend','Administration','Marketing Spend','Profit']
df.boxplot(column=cols)
plt.savefig('boxplot.jpeg')
plt.clf() #clear image

states_df=df.groupby('State')
for state,states_df in states_df:
    cols=['R&D Spend','Administration','Marketing Spend','Profit']
    states_df.boxplot(column=cols)
    plt.savefig(f'boxplot_{state}.jpeg')
    plt.clf() #clear image

from scipy import stats

df_california=df[df["State"]=="California"] 
df_newyork=df[df["State"]=="New York"] 
df_florida=df[df["State"]=="Florida"]   

profit_newyork=df_newyork["Profit"].values
profit_florida=df_florida["Profit"].values
profit_california=df_california["Profit"].values

stat,p_value = stats.f_oneway(profit_newyork,profit_florida,profit_california)
print("p value:",p_value)
#if < alpha,reject the null hypothesis of the same mean


####