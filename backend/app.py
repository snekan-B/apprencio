from math import fabs
from urllib import request
from flask  import Flask,request
import json
from flask_cors import CORS
import pickle 
import pandas as pd
import pathlib
app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    data_dir = pathlib.Path("input.csv")
    data1=pd.read_csv(data_dir)
    data1['Average'] = data1.mean(axis=1)
    data1.drop(['Monday','Tuesday','Wednesday','Thursday','Friday'],axis = 1, inplace = True)
    
    model = pickle.load(open('model.pkl','rb'))
    if(model.predict(data1) == 0):
        return  {"output":"You not worked enough hours"}
    else:
        return {"output":"You worked enough hours"}

@app.route("/input", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        data=json.loads(request.data)

        convertJsonToCsv(data)
        return "Input Fetched!!"





def convertJsonToCsv(jsonData):
    dfs = []
    dfs.append(pd.DataFrame([jsonData]))
    df = pd.concat(dfs, ignore_index=True, sort=False)
    df.drop(['userName'], 
        axis = 1, inplace = True)
    df.to_csv('input.csv',index=False)







