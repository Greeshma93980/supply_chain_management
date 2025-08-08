from fastapi import FastAPI,File,UploadFile
from fastapi.responses import JSONResponse 
import pandas as pd 
from prophet import Prophet 
import io 
app=FastAPI()
@app.post("/forecast")
async def forecast_sales(file:UploadFile=File(...)):
    try:
        contents=await file.read()
        df=pd.read_csv(io.StringIO(contents.decode('utf-8')))  #obj to str conversion uses utf-8
        if 'date' not in df.columns or 'demand' not in df.columns:
            return JSONResponse(status_code=400,content={"error":"csv doesnt consists of cols"})
        #prepare data 
        df['ds']=pd.to_datetime(df['date'])
        df['y']=df['demand']
        df=df[['ds','y']]
        #prepare model
        model=Prophet()
        model.fit(df)
        #forecast model 
        future=model.make_future_dataframe(periods=100)
        forecast=model.predict(future)
        #fetch text bases result 
        forecast_res=forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(100)
        result=forecast_res.to_dict(orient='records')
        return {"forecast":result}

    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})