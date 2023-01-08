import streamlit as st
import pickle
from flask import Flask,request

st.title("Customer Segmentation")
model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def homepage():
    return 'API Server Launched'

@app.route('/predict',methods=['GET'])
def predict():
    Gender=str(request.args.get("Enter Gender"))
    Age=float(request.args.get("Enter Age"))
    Annual_Income=float(request.args.get("Enter Income"))
    data=[[Gender,Age,Annual_Income]]
    result=model.predict(data)[0]
    return result

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )