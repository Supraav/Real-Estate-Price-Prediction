from flask import Flask,render_template,request
import flask
import pickle
import pandas as pd
import numpy as np
import sklearn

app=Flask(__name__)
app.debug=True

house=pd.read_csv("withcity.csv")
model=pickle.load(open('test_model.pkl','rb'))


@app.route('/')
def home():
    return render_template('houses.html')

@app.route('/predict',methods=["GET","POST"])
def predict():
    if request.method=="POST":
        Landsize=int(flask.request.form['landsize'])
        Livingsize=int(flask.request.form['livingsize'])
        Bathrooms=int(flask.request.form['bathroom'])
        Floors=int(flask.request.form['floors'])
        View=int(flask.request.form['view'])
        if View == 0:
            answer='Poor'
        elif View == 1:
            answer='Fair'
        elif View == 2:
            answer = 'Good'
        elif View ==3:
            answer = 'Very Good'
        else:
            answer = 'Excellent'

        Condition=int(3)
        basement=int(flask.request.form['basementsize'])
        # print('hello')
        Livingsize_above=int(Livingsize-basement)
        print(Livingsize_above)
        # Latitude=float(flask.request.form['latitude'])
        Bedrooms=int(flask.request.form['bedrooms'])
        # Longitude=float(flask.request.form['longitude'])
        underground=int(flask.request.form['underground'])
        Renovated=int(flask.request.form['renovated'])
        City=flask.request.form['city']
        print(type(basement))
        print(Renovated)
        print(answer)

        dict={'Bellevue':0,
              'Black_Diamond':0, 
              'Bothell':0, 'Carnation':0,
              'Duvall':0,'Enumclaw':0, 'Fall_City':0, 'Federal_Way':0, 'Issaquah':0,'Kent':0, 'Kirkland':0,
              'Maple_Valley':0, 'Medina':0,
                'Mercer_Island':0, 'North_Bend':0, 'Redmond':0, 'Renton':0,
                'Seattle':0, 'Shoreline':0, 'Snoqualmie':0, 'Tukwila':0,
                'Vashon':0, 'Woodinville':0, 'Yarrow_Point':0
              }
        
        dict_lat={'Bellevue':47.6194,
              'Black_Diamond':47.342, 
              'Bothell':47.7379, 'Carnation':47.6499,
              'Duvall':47.7392,'Enumclaw':47.2098, 'Fall_City':47.5643, 'Federal_Way':47.3097, 'Issaquah':47.5677,
              'Kent':47.3875, 'Kirkland':47.7159,'Maple_Valley':47.3684, 'Medina':47.639,
                'Mercer_Island':47.5786, 'North_Bend':47.4787, 'Redmond':47.6168, 'Renton':47.4556,
                'Seattle':47.721, 'Shoreline':47.7025, 'Snoqualmie':47.5319, 'Tukwila':47.5112,
                'Vashon':47.4683, 'Woodinville':47.7564, 'Yarrow_Point':47.6294,
              }
        
        dict_long={'Bellevue':-122.151,
              'Black_Diamond':-122.025, 
              'Bothell':-122.233, 'Carnation':-121.909,
              'Duvall':-121.966,'Enumclaw':-122.004, 'Fall_City':-121.897, 'Federal_Way':-122.327, 'Issaquah':-122.003,
              'Kent':-122.161, 'Kirkland':-122.165,'Maple_Valley':-122.031, 'Medina':-122.236,
                'Mercer_Island':-122.229, 'North_Bend':-121.723, 'Redmond':-122.045, 'Renton':-122.157,
                'Seattle':-122.319, 'Shoreline':-122.341, 'Snoqualmie':-121.85, 'Tukwila':-122.257,
                'Vashon':-122.438, 'Woodinville':-122.144, 'Yarrow_Point':-122.218,
              }
        
        dict[City]=1
        # print(type(dict[City]))
        # exit()

# ['Bellevue','Black_Diamond', 'Bothell', 'Carnation', 'Duvall','Enumclaw', 'Fall_City', 'Federal_Way', 'Issaquah','Kent', 'Kirkland', 'Maple_Valley', 'Medina',
# 'Mercer_Island', 'North_Bend', 'Redmond', 'Renton',
#        'Seattle', 'Shoreline', 'Snoqualmie', 'Tukwila',
#        'Vashon', 'Woodinville', 'Yarrow_Point']
        


# ['Bellevue',
#        'Black Diamond', 'Bothell', 'Carnation', 'Duvall', 'Enumclaw',
#        'Fall City', 'Federal Way', 'Issaquah', 'Kent', 'Kirkland',
#        'Maple Valley', 'Medina', 'Mercer Island', 'North Bend', 'Redmond',
#        'Renton', 'Seattle', 'Shoreline', 'Snoqualmie', 'Tukwila', 'Vashon',
#        'Woodinville', 'Yarrow Point']



        features=['Bedrooms', 'Bathrooms', 'Landsize', 'Livingsize', 'Floors', 'View','Condition'
        'Livingsize_above','basement', 'Lattitude', 'Longtitude','underground', 'Renovated','Bellevue','Black_Diamond', 
        'Bothell', 'Carnation', 'Duvall','Enumclaw', 'Fall_City', 'Federal_Way', 'Issaquah','Kent', 'Kirkland', 'Maple_Valley', 
        'Medina','Mercer_Island', 'North_Bend', 'Redmond', 'Renton','Seattle', 'Shoreline', 'Snoqualmie', 'Tukwila',
       'Vashon', 'Woodinville', 'Yarrow_Point']


        

        # Latitude=(Latitude/100.0)*(47.77760-47.15590)+47.15590	
        # Longitude=(Longitude/100.0)*(-121.31500-(-122.51200))-122.51200
        # print(City)
        final_features=[[Bedrooms,Bathrooms,Landsize,Livingsize,Floors,View,Condition,
        Livingsize_above,basement,dict_lat[City],dict_long[City],underground,Renovated,dict['Bellevue'],dict['Black_Diamond'], 
        dict['Bothell'], dict['Carnation'],dict['Duvall'],dict['Enumclaw'],dict['Fall_City'],dict['Federal_Way'],dict['Issaquah'],dict['Kent'],dict['Kirkland'],dict['Maple_Valley'],
        dict['Medina'],dict['Mercer_Island'],dict['North_Bend'],dict['Redmond'],dict['Renton'],dict['Seattle'],dict['Shoreline'], dict['Snoqualmie'], dict['Tukwila'],
       dict['Vashon'], dict['Woodinville'],dict['Yarrow_Point']]]



    #     dict['Bellevue'],dict['Black_Diamond'], 
    #     dict['Bothell'], dict['Carnation'],dict['Duvall'],dict['Enumclaw'],dict['Fall_City'],dict['Federal_Way'],dict['Issaquah'],dict['Kent'],dict['Kirkland'],dict['Maple_Valley'],
    #     dict['Medina'],dict['Mercer_Island'],dict['North_Bend'],dict['Redmond'],dict['Renton'],dict['Seattle'],dict['Shoreline'], dict['Snoqualmie'], dict['Tukwila'],
    #    dict['Vashon'], dict['Woodinville'],dict['Yarrow_Point']
        
        print(final_features)
        prediction=model.predict(final_features)[0] 
        op=round(prediction,2)
        return render_template('houses.html',result=op,Bathrooms=Bathrooms,Bedrooms=Bedrooms,Landsize=Landsize,Livingsize=Livingsize,Floors=Floors,basement=basement,City=City,underground='yes' if underground else 'no', Renovated= 'yes' if Renovated else 'no',View = answer)

    return render_template('houses.html')
if __name__=='__main__':
    app.run(debug=True)