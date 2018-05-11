from flask import Flask,request,render_template
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
app=Flask(__name__)

# Importing the dataset




# @app.route('/')
# def home():
#     return "Data Mining Project"

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method=="POST":
        name=request.form['uname']
        string="welcome : "+name
        return string
    else:
        return render_template("index.html")

@app.route("/")
def mining():
   return render_template('index.html')
@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method=="POST":
        dataset = pd.read_csv('static/Finally.csv')
        X = dataset.iloc[:, [0,1,2,3,4,5]].values
        y = dataset.iloc[:, 6].values
        my_x=dataset.iloc[:, [0,1,2,3,4,5]].values
        c=[0,0,0,0,0,0]
        c[0]=request.form['c0']
        c[1]=request.form['c1']
        c[2]=request.form['c2']
        c[3]=request.form['c3']
        c[4]=request.form['c4']
        c[5]=request.form['c5']
        user_x=[c]

        from sklearn.cross_validation import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0, random_state = 0)
        print("before")
        print(user_x)
        print(my_x[7])
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        from sklearn.svm import SVC

        svm_classifier=SVC(kernel='rbf',random_state=0)
        svm_classifier.fit(X_train,y_train)
        my_pred=svm_classifier.predict(my_x)
        user_pred=svm_classifier.predict(user_x)
        print("prediction")
        print("user",user_pred)
        print("my ",my_pred[7])


        from sklearn.metrics import confusion_matrix
        result=user_pred[0]
        if (result==1):
            return render_template('fail.html')
        else:
            return render_template('success.html')
   
    else:
        return render_template('index2.html')
        
        return render_template('index2.html')
if __name__=="__main__":
    app.run()
