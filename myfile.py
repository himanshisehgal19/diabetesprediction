from flask import Flask,render_template,redirect,request
#from flask_material import Material

# EDA PKg
import pandas as pd 
import numpy as np 

# ML Pkg
import joblib

app=Flask(__name__)

model=joblib.load("model.pkl")

@app.route('/')
def index():
	return render_template("indix.html")

@app.route('/',methods=['POST'])
def marks():
	if request.method=='POST':
		hours=float(request.form['hours'])
		marks=str(model.predict([[hours]]))
	return render_template("indix.html",yourmarks=marks)
if __name__ == '__main__':
	app.run(debug=True)
	