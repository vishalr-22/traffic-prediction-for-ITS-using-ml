from flask import Flask, render_template, request, url_for, redirect, flash
from dbservice import dbservice


app = Flask(__name__)
app.secret_key = "super secret key"
db = dbservice()


@app.route('/')
def homepage():                                         # function for homepage
    if request.method=='POST':
        return render_template('homepage.html')
    return render_template('homepage.html')


@app.route('/predict',methods=['POST','GET'])
def predict():                                          # function for prediction
    if request.method=='POST':
        junction = request.form.get('junction')         #fetching junction number from the form
        vehicle = request.form.get('vehicle')           #fetching no of vehicles from the form
        lst = db.svm(junction, vehicle)
        if lst[0] == 1:                                 # Traffic condition
            return render_template('predict.html',text='Traffic Expected')
        elif lst[0] == 0:
            return render_template('predict.html',text='Traffic Not Expected')
        else:
            return render_template('predict.html',text='Invalid Credentials')
    return render_template('predict.html')

