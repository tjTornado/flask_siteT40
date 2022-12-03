# -*- coding: utf-8 -*-
from functools import wraps

from flask import Flask, request, render_template, url_for, send_from_directory, redirect, session, json, jsonify, g
import os
from datetime import timedelta
import time
import threading
import datetime
from utils import qurry_for_data, qurry_for_result
from AdminController import admin_opt
from MarketController import market_opt
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小
app.register_blueprint(admin_opt, url_prefix="/admin")
app.register_blueprint(market_opt, url_prefix="/market")



@app.route('/')
def login_html():
    return redirect('/static/login.html')


@app.route('/login',methods=["POST"])
def login():
    code = request.values.get('code')
    if code == "123":
        session["username"] = 123
        session["role"] = 1
        return jsonify({"msg":"登录成功","code":"0","url":"/static/workspace.html"})




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234, debug=False, use_reloader=False)
