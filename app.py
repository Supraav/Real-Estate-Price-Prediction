from flask import Flask,render_template,request
import flask
import pickle
import pandas as pd
import numpy as np
app=Flask(__name__)
app.debug=True

model=pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('final.html')

    if request.method=='POST':
        Bedrooms=int(flask.request.form['bedrooms'])
        Bathrooms=int(flask.request.form['bathroom'])
        Landsize=int(flask.request.form['landsize'])
        Livingsize=int(flask.request.form['livingsize'])
        Floors=int(flask.request.form['floors'])
        View=int(flask.request.form['view'])
        Livingsize_above=int(flask.request.form['abovesize'])
        Latitude=float(flask.request.form['latitude'])
        Longitude=float(flask.request.form['longitude'])
        # Livingsize15=flask.request.form['livingsize15']
        # Landsize15=flask.request.form['landsize15']
        # houseage=flask.request.form['houseage']
        underground=flask.request.form['underground']
        Renovated=flask.request.form['renovated']

    #     features=['Bedrooms', 'Bathrooms', 'Landsize', 'Livingsize', 'Floors', 'View',
    #    'Livingsize_above', 'Lattitude', 'Longtitude', 'Livingsize15', 'Landsize15', 'houseage',
    #    'underground', 'Renovated']

        Latitude=(Latitude/100.0)*(47.77760-47.15590)+47.15590	
        Longitude=(Longitude/100.0)*(-121.31500-(-122.51200))-122.51200
        final_features=np.array([[Bedrooms, Bathrooms,Landsize,Livingsize,Floors,View,Livingsize_above,Latitude,Longitude,underground,Renovated]])
        print (type(final_features[0][0]))
        print(type(Bedrooms))
        prediction=model.predict(final_features)[0]   
        return render_template('final.html',result=prediction)

if __name__=='__main__':
    app.run(debug=True)