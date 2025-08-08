import numpy as np 
import pandas as pd 
from prophet import Prophet 
import matplotlib.pyplot as plt 
df=pd.read_csv("Train.csv")
print(df.head())
#PREPARE Data for prophet model 
df['ds']=pd.to_datetime(df['order_date'])
#rename order_date to ds 
df['y']=df['units_sold']
df=df[['ds','y']]  #keep require columns for input data 
print(df.head())
#initialize and fit the model
model=Prophet()
model.fit(df)
# forecast for 30 future days 
future=model.make_future_dataframe(periods=30)
forecast=model.predict(future)
#plot forecast 
#model.plot(forecast)
#plt.title("Sales forecast")
#plt.show()
model.plot_components(forecast)
plt.show()