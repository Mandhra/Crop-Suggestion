from flask import Flask,request,render_template
import numpy as np
import pickle
import sklearn
print(sklearn.__version__)
model=pickle.load(open('Crop_recommendation.pkl','rb'))
encoder=pickle.load(open('encoder.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        Temperature=float(request.form['temperature'])
        Humidity=float(request.form['humidity'])
        ph=float(request.form['ph'])
        Rainfall=float(request.form['rainfall'])
        N=float(request.form['nitrogen'])
        P=float(request.form['potassium'])
        K=float(request.form['phosphorous'])
        
        features=np.array([[N,P,K,Temperature,Humidity,ph,Rainfall]],dtype=object)
        prediction=model.predict(features).reshape(-1,1)
        prediction = encoder.inverse_transform(prediction)

        return render_template('index.html',prediction=prediction[0])
if __name__=="__main__":
    app.run(debug=True)