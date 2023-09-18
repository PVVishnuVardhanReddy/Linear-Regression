import pandas as pd  
import seaborn as sns
df=pd.read_csv("/Users/pvenkatavishnuvardhanreddy/Desktop/houserent.csv")
sns.lmplot(x="Avg. Area Income",y="Price",data=df)
sns.lmplot(x="Avg. Area Number of Bedrooms",y="Price",data=df)
sns.lmplot(x="Avg. Area House Age",y="Price",data=df)
sns.lmplot(x="Area Population",y="Price",data=df)