# -*- coding: utf-8 -*- 
'''

@author: Administrator
'''
import os,sys
import json



# filepath_ = sys.path[0]+'\manage\\files\\banners.txt'

def file_iterator(file_name, chunk_size=262144):
     f = open(file_name, mode='r', encoding='utf-8')
     return f.read(chunk_size)
     f.close()

filepath_ = sys.path[0]+'\manage\\files\\banners.txt'
if os.path.exists(filepath_):
    textbanner=file_iterator(filepath_)
    card={}
    cards=[]
    items={} 
    cardUnit={}
    cardUnits=[]
    item=[]
    cardUnits.append(items)
    items["items"]=item
    itemvalue={}
    itemvalue["imgurl"]="imgurl"
    itemvalue["content"]="content"
    itemvalue["title"]="title"
    itemvalue["bckimgurl"]="bckimgurl"
    item.append(itemvalue)
    #banners
    f = open(filepath_, mode='r', encoding='utf-8')
    bannerjson = json.load(f)
#     cardUnit["banners"]=bannerjson
    
    cardUnit["cardUnits"]=cardUnits
    cards.append(bannerjson)
    cards.append(cardUnit)
    card["cards"]=cards 
    jsonStr = json.dumps(card) 
    print (jsonStr)
    
import json
import xinge_push

#create XingeApp
xinge = xinge_push.XingeApp(0, 'secret')

#build your message
msg = xinge_push.Message()
msg.type = xinge_push.MESSAGE_TYPE_ANDROID_NOTIFICATION
msg.title = 'some title'
msg.content = 'some content'

#call restful API
ret_code, error_msg = xinge.PushSingleDevice('some_token', msg)
if ret_code:
    print ("push failed! retcode: {}, msg: {}".format(ret_code, error_msg))
else:
    print ("push successfully!")

    
# setting = json.load(f)
# family = setting['BaseSettings']['size']   
# size = setting['fontSize']  
# filepath_ = os.path.abspath('.')+'\manage\\files\per.txt'
# print (setting)
 
  

# print('sssss%s'%('a'),'ttt')
# print (os.path.exists(filepath_))
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print("hello,%s!"%x)    
# print ('{}'.format(os.path.basename(filepath_)))
# file_object = open(filepath_, mode='r', encoding='UTF-8')
# try:
#      all_the_text = file_object.read( )
#      print (all_the_text)
# finally:
#      file_object.close( )
# import sqlite3
# 
# # test.db is a file in the working directory.
# conn = sqlite3.connect("test.db")
# 
# c = conn.cursor()
# 
# # create tables
# c.execute('''CREATE TABLE category
#       (id int primary key, sort int, name text)''')
# c.execute('''CREATE TABLE book
#       (id int primary key, 
#        sort int, 
#        name text, 
#        price real, 
#        category int,
#        FOREIGN KEY (category) REFERENCES category(id))''')
# 
# # save the changes
# conn.commit()
# 
# # close the connection with the database
# conn.close()
# import sqlite3
# 
# conn = sqlite3.connect("test.db")
# c    = conn.cursor()
# 
# books = [(1, 1, 'Cook Recipe', 3.12, 1),
#             (2, 3, 'Python Intro', 17.5, 2),
#             (3, 2, 'OS Intro', 13.6, 2),
#            ]
# 
# # execute "INSERT" 
# c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
# 
# # using the placeholder
# # c.execute("INSERT INTO category VALUES (?, ?, ?)", [(2, 2, 'computer')])
# 
# # execute multiple commands
# c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
# 
# conn.commit()
# conn.close()

# import sqlite3
# 
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# 
# # retrieve one record
# c.execute('SELECT name FROM category ORDER BY sort')
# print(c.fetchone())
# print(c.fetchone())
# 
# # retrieve all records as a list
# c.execute('SELECT * FROM book WHERE book.category=1')
# print(c.fetchall())
# 
# # iterate through the records
# for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
#     print(row)
