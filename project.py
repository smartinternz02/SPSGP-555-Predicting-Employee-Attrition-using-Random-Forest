from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__) #your application
rf=pickle.load(open('demo.pkl','rb'))


@app.route('/') # default route
def home():
    return render_template("proj.html")
#satisfaction_level	last_evaluation	number_project	average_montly_hours	
#time_spend_company	Work_accident	left	promotion_last_5years	Department	salary

@app.route('/predict',methods=['post'])
def predict():
    satisfaction_level=float(request.form['satisfaction_level'])
    last_evaluation=float(request.form['last_evaluation'])
    number_project=float(request.form['number_project'])
    average_montly_hours=float(request.form['average_montly_hours'])
    time_spend_company=float(request.form['time_spend_company'])
    Work_accident=float(request.form['Work_accident'])
    promotion_last_5years=float(request.form['promotion_last_5years'])
    salary=float(request.form['salary'])
    Department=float(request.form['Department'])
    
    
    #print(rspend,Administration,Marketing_Spend,State)
    a=np.array([[satisfaction_level,last_evaluation,number_project,average_montly_hours,time_spend_company,Work_accident,promotion_last_5years,salary,Department]])
    print(a)
    result=rf.predict(a)
    print(result)
    index=['Left','Stay']
    result=index[result[0]]
    
    
    return render_template('proj.html',x="The employe will be :"+str(result))

if __name__ == '__main__':
    app.run(debug=True) # you are running your app

