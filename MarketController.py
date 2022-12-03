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

market_opt = Blueprint('market_opt', __name__)

def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        #if 'username' in session:
        if True:
            return func(*args, **kwargs)
        else:
            return jsonify({"msg":"登录状态失效","code":"-1","url":"/"})
    return check_login


@market_opt.route('/materialshow', methods=['GET','POST'])
@is_login
def materialshow():
    res = qurry_for_data(f"select * from `material`")
    return jsonify({"msg": "查询成功", "code": "0","data":res})

@market_opt.route('/shelvesshow', methods=['GET','POST'])
@is_login
def shelvesshow():
    res = qurry_for_data(f"select * from `shelves` order  by id")
    for i in range(len(res)):
        if res[i]["amount"] == 0:
            res[i]["sort"] = "空"
    res2 = qurry_for_data(f"select * from `material`")
    for i in range(len(res2)):
        for j in range(len(res)):
            if res2[i]['name'] == res[j]["sort"]:
                if "number" not in res2[i].keys():
                    res2[i]["number"] = res[j]["amount"]
                else:
                    res2[i]["number"] = res2[i]["number"] + res[j]["amount"]
    return jsonify({"msg": "查询成功", "code": "0","data":res,"all":res2})


@market_opt.route('/materialmodify', methods=['POST'])
@is_login
def materialmodify():
    id = request.values.get('id')
    minimum = request.values.get('minimum')
    if id == None or minimum == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    res = qurry_for_data(f"select * from `material` where id={int(id)}")
    if len(res) == 0:
        return jsonify({"msg": "该物料不存在！", "code": "-1"})
    else:
        qurry_for_result(f"update `material` set minimum={int(minimum)} where id={int(id)}")
        return jsonify({"msg": "修改成功！", "code": "0"})

@market_opt.route('/shelvesadd', methods=['POST'])
@is_login
def shelvesadd():
    username = session.get('username')
    data = request.values.get('data')
    if data == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    print(data)
    data = json.loads(data)

    for i in data:
        qurry_for_result(f"update `shelves` set `sort`='{i['sort']}',`presets`=`presets`+{int(i['amount'])}-`amount`,`amount`={int(i['amount'])} where `name`='{i['name']}'")
        qurry_for_result(f"insert into `feed_log` (`username`,`shelves_name`,`sort`,`amount`)values('{username}','{i['name']}','{i['sort']}',{int(i['amount'])})")
    return jsonify({"msg": "补料成功！", "code": "0"})

@market_opt.route('/feed_log', methods=['GET','POST'])
@is_login
def feedlog():
    page = request.values.get('page')
    maxnum = request.values.get('maxnum')
    if page == None:
        page = 1
    if maxnum == None:
        maxnum = 20
    res = qurry_for_data(f"select * from `feed_log` order by id desc")
    left = (page - 1) * maxnum
    right = page * maxnum
    if left > len(res):
        res = []
    if right > len(res):
        right = len(res)
    return jsonify({"msg": "查询成功", "code": "0","data":res[left:right],"maxSize":len(res),"pageSize":int(len(res)/maxnum)})


