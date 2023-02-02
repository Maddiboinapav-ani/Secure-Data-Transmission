from flask import Flask,render_template,redirect,request

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/dashboard')
def dashboardpage():
    return render_template('dashboard.html')

@app.route('/sender')
def senderpage():
    return render_template('sender.html')

@app.route('/receiver')
def receiverpage():
    return render_template('receiver.html')

@app.route('/logout')
def logoutpage():
    return redirect('/')
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)