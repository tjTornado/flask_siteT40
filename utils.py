# encoding: utf-8
'''
@author: tracerboy
@contact: tracerboy@163.com
@application:
@time: 2022/11/29 11:55
'''
datebase = {}
datebase['address'] = "47.94.89.200"
datebase['user'] = "T40"
datebase['passwd'] = "8PjitPFSj8W33JfP"
datebase['db'] = "t40"
import pymysql


def qurry_for_data(sql):
    # print(sql)
    conn = pymysql.connect(host=datebase['address'], user=datebase['user'], passwd=datebase['passwd'],
                           db=datebase['db'], charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 执行完毕返回的结果集默认以元组显示
    res = cursor.execute(sql)
    dict = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return dict


def qurry_for_result(sql):
    conn = pymysql.connect(host=datebase['address'], user=datebase['user'], passwd=datebase['passwd'],
                           db=datebase['db'], charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 执行完毕返回的结果集默认以元组显示
    res = cursor.execute(sql)
    dict = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return res
