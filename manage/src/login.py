#coding=utf-8
'''
Created on 2017��6��12��
http://192.168.30.25:8080/login/?account=000&psw=%22%22
@author: Administrator
'''

from manage.src.userdb import * 
from manage.src.logintoken import *
from manage.src.Responsejson import *   
def login(request):  
    account = request.GET.get('account')
    psw = request.GET.get('psw')
    if not psw:
       return resultNone('psw','') 
    if not account:
       return resultNone('account','null')  
    conn = createDB()
    user = selectDB(conn,account)
    if not user:
       conn.close
       return resultNone('account','uer has unregister')   
    token = getlogintoken(account)
    updatetokenDB(conn,account,token)
    conn.close 
    return resultLogin(token,user)
