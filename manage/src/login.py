#coding=utf-8
'''
Created on 2017��6��12��

@author: Administrator
'''
import re
import urllib.request  
import json
import time
import os,sys
import sqlite3

from django.http import HttpResponse  
from django.http import StreamingHttpResponse 
def login(request):  
       # do something...
    conn = createDB()
    selectDB(conn)
    filepath_ = sys.path[0]+'\manage\\files\Ads.txt'
    print(filepath_)
    def file_iterator(file_name, chunk_size=262144):
        f = open(filepath_, mode='r', encoding='GBK')
        while True:
             c = f.read(chunk_size)
             if c:
                 yield c
             else:
                 break
        f.close()
    if not os.path.exists(filepath_):   
       response_data = {}  
       response_data['result'] = 'failed'  
       response_data['message'] = 'You messed up'  
       return HttpResponse(json.dumps(response_data), content_type="application/json")    
    return HttpResponse(file_iterator(filepath_), content_type="application/json")   
 
def createDB():
# test.db is a file in the working directory.
    conn = sqlite3.connect("user.db")
    
#     c = conn.cursor()
    # create tables
    conn.execute('''CREATE TABLE IF NOT EXISTS users
         (id int primary key, sort int, name text,location text)''')
    return conn
#     c.execute('''CREATE TABLE book
#          (id int primary key, 
#           sort int, 
#           name text, 
#           price real, 
#           category int,
#           FOREIGN KEY (category) REFERENCES category(id))''')
 
# save the changes 
def selectDB(conn):
    c = conn.cursor()
    c.execute('SELECT name FROM users ORDER BY sort')
    
    rows = c.fetchall()
    #遍历数据也不变（比上一个更直接一点）
    for row in rows:
        #这里，可以使用键值对的方法，由键名字来获取数据
        print ("%s %s" % (row["Id"], row["Name"]))