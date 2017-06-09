# -*- coding: utf-8 -*- 
'''

@author: Administrator
'''
import os,sys
import json

filepath_ = os.path.abspath('.')+'\manage\\files\per.txt'
# print (sys.(filepath_))
 
  

print('sssss%s'%('a'),'ttt')
print (os.path.exists(filepath_))
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("hello,%s!"%x)    
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