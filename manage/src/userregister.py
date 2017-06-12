#coding=utf-8
'''
Created on 2017��6��12��
http://192.168.30.25:8080/register/?account=000&psw=%22%22
@author: Administrator
'''
import os,sys
import sqlite3
import json

from django.http import HttpResponse  
from django.http import StreamingHttpResponse 
def userregister(request):  
       # do something...
    account = request.GET.get('account')
    psw = request.GET.get('psw')
    if not psw:
       return resultNone('psw','') 
    if not account:
       return resultNone('account','')    
    
    conn = createDB()
    index = selectDB(conn,account)
    if index:
       return resultNone('account','uer has ') 
    addDB(conn,account,psw)
    conn.close
    response_data = {}  
    response_data['result'] = 'failed'  
    response_data['message'] = 'You messed up'  
    return HttpResponse(json.dumps(response_data), content_type="application/json")    

def createDB():
# test.db is a file in the working directory.
    conn = sqlite3.connect("user.db")
    
#     c = conn.cursor()
    # create tables
    conn.execute('''CREATE TABLE IF NOT EXISTS users
         (id INTEGER PRIMARY KEY, sort int, account text,location text,psw text,sex int,img text,phone int,name text,age int)''')
    return conn
def selectDB(conn,account):
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE  account = '+account+' ORDER BY sort')
    rows = c.fetchall()
    #遍历数据也不变（比上一个更直接一点）
    newaccount = None
    for row in rows:
        newaccount = row[2]
        print ("%s %s" % (row[0], newaccount))
        break
    if not newaccount:
        return  False 
    return  True    
        
def addDB(conn,account,psw):
    c = conn.cursor()
    conn.execute('INSERT INTO users(account,psw)values('+account+','+psw+')')
    conn.commit()
def resultNone(data,msg):
    response_data = {}  
    response_data['result'] = 0  
    response_data[data] = msg  
    return HttpResponse(json.dumps(response_data), content_type="application/json") 