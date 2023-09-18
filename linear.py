import pandas as pd  
from sklearn.linear_model import LinearRegression
df=pd.read_csv("/Users/pvenkatavishnuvardhanreddy/Desktop/houserent.csv")
lr=LinearRegression()
lr.fit(df[["Avg. Area Income","Avg. Area Number of Bedrooms","Avg. Area House Age","Area Population"]],df["Price"])
def linearreg(inc,age,bed,popu):
    return lr.predict([[inc,age,bed,popu]])

