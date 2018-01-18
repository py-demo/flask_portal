# coding:utf8
from flask import Flask, render_template, json, jsonify
from test.api_menus import menu
from test.api_datagrid import datagrid

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/menus', methods=['POST', 'GET'])
def menus():
    return render_template('page-menus.html')


@app.route('/api_datagrid', methods=['POST', 'GET'])
def api_datagrid():
    return jsonify(datagrid)


@app.route('/api_menus', methods=['POST', 'GET'])
def api_menus():
    return jsonify(menu)

@app.route('/form', methods=['POST', 'GET'])
def form():
    return ''


if __name__ == "__main__":
    app.run()
