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
         (uid INTEGER PRIMARY KEY, account text,location text,psw text,sex int,img text,phone text,name text,age int,token text)''')
    return conn  
def selectDB(conn,account):
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE  account = '+account+' ORDER BY id')
    rows = c.fetchall()
    #遍历数据也不变（比上一个更直接一点）
    for row in rows:
        user={}
        user["location"]=(not row[2] )and row[2] or ''
        user["sex"]=(not row[4] )and row[4] or 0
        user["img"]=(not row[5] )and row[5] or ''
        user["phone"]=(not row[6] )and row[6] or ''
        user["name"]=(not row[7] )and row[7] or ''
        user["age"]=(not row[8] )and row[8] or 0
        user["token"]=(not row[9] )and row[9] or ''
        user["account"]=(not row[1] )and row[1] or ''
        user["uid"]=(not row[0] )and row[0] or 0
        return user
        break
    return None
 
def addDB(conn,account,psw):
    conn.execute('INSERT INTO users(account,psw)values('+account+','+psw+')')
    conn.commit()
def updatetokenDB(conn,account,token):
    conn.execute("UPDATE users SET token = '"+token+"' WHERE account = "+account)
    conn.commit()    