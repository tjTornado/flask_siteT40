# encoding: utf-8
'''
@author: tracerboy
@contact: tracerboy@163.com
@application:
@time: 2022/11/29 12:01
'''
import json
from functools import wraps

from flask import Blueprint, request, session, redirect, jsonify
from utils import qurry_for_data, qurry_for_result

call_opt = Blueprint('call_opt', __name__)

def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        if 'username' in session:
            return func(*args, **kwargs)
        else:
            return jsonify({"msg":"登录状态失效","code":"-1","url":"/"})
    return check_login


@call_opt.route('/materialshow', methods=['GET','POST'])
@is_login
def materialshow():
    res = qurry_for_data(f"select * from `material`")
    return jsonify({"msg": "查询成功", "code": "0","data":res})

@call_opt.route('/shelvesshow', methods=['GET','POST'])
@is_login
def shelvesshow():
    res = qurry_for_data(f"select * from `shelves`")
    return jsonify({"msg": "查询成功", "code": "0","data":res})

