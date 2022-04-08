#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    #return "Hello World"

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,7)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='Banana'
        elif int(result)==2:
            prediction='Blackgram'
        elif int(result)==3:
            prediction ='Chickpea'
        elif int(result)==4:
            prediction ='Coconut'
        elif int(result)==5:
            prediction ='Coffee'
        elif int(result)==6:
            prediction ='Cotton'
        elif int(result)==7:
            prediction ='Grape'
        elif int(result)==8:
            prediction = 'Jute'
        elif int(result)==9:
            prediction = 'Kidneybeans'
        elif int(result)==10:
            prediction = 'Lentil'
        elif int(result)==11:
            prediction = 'Maize'
        elif int(result)==12:
            prediction = 'Mango'
        elif int(result)==13:
            prediction = 'Mothbeans'
        elif int(result)==14:
            prediction = 'Mungbeans'
        elif int(result)==15:
            prediction = 'Muskmelon'
        elif int(result)==16:
            prediction = 'Orange'
        elif int(result)==17:
            prediction = 'Papaya'
        elif int(result)==18:
            prediction = 'Pigeonpeas'
        elif int(result)==19:
            prediction ='Pomegranate'
        elif int(result)==20:
            prediction ='Rice'
        elif int(result)==21:
            prediction = 'Watermelon'
        else:
            prediction='Apple'
            
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
	app.run(debug=True)