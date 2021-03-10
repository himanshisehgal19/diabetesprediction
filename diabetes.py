from flask import Flask,render_template,redirect,request
import pandas as pd 
import numpy as np
import joblib

app=Flask(__name__)
model=joblib.load("model.pkl")
@app.route('/')
def index():
	return render_template("indix.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        var1=int(request.form['preg'])
        var2=int(request.form['glucose'])
        var3=int(request.form['bldp'])
        var4=int(request.form['skinth'])
        var5=int(request.form['insulin'])
        var6=float(request.form['bmi'])
        var7=float(request.form['dpf'])
        var8=int(request.form['age'])
        listofdia=[var1,var2,var3,var4,var5,var6,var7,var8]
        prediction=str(model.predict([listofdia]))
    return render_template("indix.html", predicted=prediction[1])
if __name__== '__main__':
    app.run(debug=True)
