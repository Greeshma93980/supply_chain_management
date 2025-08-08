import streamlit as st 
import pandas as pd 
from prophet import Prophet 
import matplotlib.pyplot as plt 
st.set_page_config(page_title="Prophet model")
st.title("Sales forecast using  prophet")
uploaded_file=st.file_uploader("upload your csv")
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.subheader("Raw data")
    st.write(df.head())
    df['ds']=pd.to_datetime(df['order_date'])
    df['y']=df['units_sold']
    df=df[['ds','y']]
    model=Prophet()
    model.fit(df)
    future=model.make_future_dataframe(periods=90)
    forecast=model.predict(future)
    st.subheader("Forecast")
    fig1=model.plot(forecast)
    st.pyplot(fig1)
    st.subheader("forecast components")
    fig2=model.plot_components(forecast)
    st.pyplot(fig2)