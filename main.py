from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
 
app = FastAPI()
 
class datas(BaseModel):
    carat : float
    cut : int
    color : int
    clarity : int
    depth : float
    table : float
    x : float
    y : float
    z : float
 
@app.post('/predict')
async def predict_species(value: datas):
    data = value.dict()
    loaded_model = pickle.load(open('clas.pkl', 'rb'))
    data_in = [[data['carat'], data['cut'], data['color'], data['clarity'], data['depth'], data['table'], data['x'], data['y'], data['z']]]
    prediction = loaded_model.predict(data_in)
    print(prediction)
    return  prediction[0]
    