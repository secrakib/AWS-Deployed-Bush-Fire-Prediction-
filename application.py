from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

#import ridge.pkl and scalar.pkl
ridge_model=pickle.load(open('Model/model.pkl','rb'))
scalar=pickle.load(open('Model/scaler.pkl','rb'))

'''
app.route("/")
def index():
    return render_template('index.html')
'''
#prediction
@app.route("/",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        BUI = float(request.form.get('BUI'))
        Classes = float(request.form.get('Classes'))  
        Region = float(request.form.get('Region')) 

        scaled_data=scalar.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI,BUI, Classes, Region]])
        result=ridge_model.predict(scaled_data)

        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
