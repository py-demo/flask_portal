# coding:utf8
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/menus',methods=['GET','POST'])
def menus():
    return render_template('page-menus.html')

if __name__=="__main__":
    app.run()