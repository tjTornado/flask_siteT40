# encoding: utf-8
'''
@author: tracerboy
@contact: tracerboy@163.com
@application:
@time: 2022/11/29 12:01
'''
from functools import wraps
from flask import Blueprint, request, session, redirect, jsonify
from utils import qurry_for_data, qurry_for_result

admin_opt = Blueprint('admin_opt', __name__)

def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        #if 'username' in session:
        if True:
            return func(*args, **kwargs)
        else:
            return jsonify({"msg":"登录状态失效","code":"-1","url":"/"})
    return check_login


@admin_opt.route('/getinfo', methods=['GET','POST'])
@is_login
def getip():
    res = qurry_for_data(f"select * from `ip`")
    return jsonify({"msg": "查询成功", "code": "0","ip":res[0]["address"],"robot":res[0]["robot"]})

@admin_opt.route('/setip', methods=['GET','POST'])
@is_login
def setip():
    ip = request.values.get('ip')
    if ip == None:
        return jsonify({"msg": "部分参数为空", "code": "-1"})
    qurry_for_result(f"update `ip` set `address`='{ip}' where id=1")
    return jsonify({"msg": "设置成功成功", "code": "0","robot":["A","B","C"]})

@admin_opt.route('/setrobot', methods=['GET','POST'])
@is_login
def setrobot():
    robot = request.values.get('robot')
    if robot == None:
        return jsonify({"msg": "部分参数为空", "code": "-1"})
    qurry_for_result(f"update `ip` set `robot`='{robot}' where id=1")
    return jsonify({"msg": "设置成功成功", "code": "0"})


@admin_opt.route('/usershow', methods=['GET','POST'])
@is_login
def usershow():
    res = qurry_for_data(f"select * from `user`")
    return jsonify({"msg": "查询成功", "code": "0","data":res})


@admin_opt.route('/useradd', methods=['POST'])
@is_login
def useradd():
    username = request.values.get('username')
    role = request.values.get('role')
    if username == None or role == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    res = qurry_for_data(f"select * from `user` where username='{username}'")
    if len(res) == 0:
        qurry_for_result(f"insert into `user` (`username`,`role`)values('{username}',{int(role)})")
        return jsonify({"msg": "新增用户成功", "code": "0"})
    else:
        return jsonify({"msg": "该用户名已存在！", "code": "-1"})

@admin_opt.route('/userdel', methods=['POST'])
@is_login
def userdel():
    userid = request.values.get('userid')
    if userid == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    res = qurry_for_data(f"select * from `user` where id='{int(userid)}'")
    if len(res) == 0:
        return jsonify({"msg": "该用户不存在，请勿重复删除！", "code": "-1"})
    else:
        qurry_for_result(f"delete from `user` where id='{int(userid)}'")
        return jsonify({"msg": "删除成功！", "code": "0"})


@admin_opt.route('/usermodify', methods=['POST'])
@is_login
def usermodify():
    userid = request.values.get('userid')
    role = request.values.get('role')
    if userid == None or role == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    res = qurry_for_data(f"select * from `user` where id={int(userid)}")
    if len(res) == 0:
        return jsonify({"msg": "该用户不存在！", "code": "-1"})
    else:
        qurry_for_result(f"update `user` set role={int(role)} where id={int(userid)}")
        return jsonify({"msg": "修改成功！", "code": "0"})




@admin_opt.route('/materialshow', methods=['GET','POST'])
@is_login
def materialshow():
    res = qurry_for_data(f"select * from `material`")
    return jsonify({"msg": "查询成功", "code": "0","data":res})


@admin_opt.route('/materialadd', methods=['POST'])
@is_login
def materialadd():
    name = request.values.get('name')
    minimum = request.values.get('minimum')
    if name == None or minimum == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    res = qurry_for_data(f"select * from `material` where `name`='{name}'")
    if len(res) == 0:
        qurry_for_result(f"insert into `material` (`name`,`minimum`)values('{name}',{int(minimum)})")
        return jsonify({"msg": "新增物料成功", "code": "0"})
    else:
        return jsonify({"msg": "该物料名已存在！", "code": "-1"})

@admin_opt.route('/materialdel', methods=['POST'])
@is_login
def materialdel():
    id = request.values.get('id')
    if id == None:
        return jsonify({"msg":"部分参数为空","code":"-1"})
    res = qurry_for_data(f"select * from `material` where id={int(id)}")
    if len(res) == 0:
        return jsonify({"msg": "该物料不存在，请勿重复删除！", "code": "-1"})
    else:
        qurry_for_result(f"delete from `material` where id={int(id)}")
        return jsonify({"msg": "删除成功！", "code": "0"})


@admin_opt.route('/materialmodify', methods=['POST'])
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
