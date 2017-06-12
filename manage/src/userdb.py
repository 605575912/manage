#coding=utf-8
'''
Created on 2017��6��12��

@author: Administrator
'''

import sqlite3
def createDB():
# test.db is a file in the working directory.
    conn = sqlite3.connect("user.db")
    
#     c = conn.cursor()
    # create tables
    conn.execute('''CREATE TABLE IF NOT EXISTS users
         (id INTEGER PRIMARY KEY, account text,location text,psw text,sex int,img text,phone int,name text,age int,token text)''')
    return conn  
def selectDB(conn,account):
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE  account = '+account+' ORDER BY id')
    rows = c.fetchall()
    #遍历数据也不变（比上一个更直接一点）
    for row in rows:
        user={}
        user["location"]=(not row[2] )and row[2] or ''
        user["sex"]=row[4]
        user["img"]=row[5]
        user["phone"]=row[6]
        user["name"]=row[7]
        user["age"]=row[8]
        user["token"]=row[9]
        user["account"]=row[1]
        return user
        break
    return None
 
def addDB(conn,account,psw):
    conn.execute('INSERT INTO users(account,psw)values('+account+','+psw+')')
    conn.commit()
def updatetokenDB(conn,account,token):
    conn.execute("UPDATE users SET token = '"+token+"' WHERE account = "+account)
    conn.commit()    