# coding:utf8
from flask import Flask, render_template, Request, json, jsonify
from test.api_menus import menu
from test.api_datagrid import datagrid

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index_login():
    return render_template('login.html')


@app.route('/home', methods=['POST', 'GET'])
def page_home():
    return render_template('home.html')


@app.route('/menus', methods=['POST', 'GET'])
def page_menus():
    return render_template('page-menu.html')


@app.route('/list', methods=['POST', 'GET'])
def page_list():
    return render_template('page-list.html')


@app.route('/api_datagrid', methods=['POST', 'GET'])
def api_datagrid():
    return jsonify(datagrid)


@app.route('/api_menus', methods=['POST', 'GET'])
def api_menus():
    return jsonify(menu)


@app.route('/form', methods=['POST', 'GET'])
def api_form():
    return jsonify({
        'code': 200,
        'msg': '数据保存成功！',
        'data': []
    })


if __name__ == "__main__":
    app.run()
