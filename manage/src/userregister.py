#coding=utf-8
'''
Created on 2017��6��12��
http://192.168.30.25:8080/register/?account=000&psw=%22%22
@author: Administrator
'''



from manage.src.userdb import * 
from manage.src.Responsejson import * 
def userregister(request):  
       # do something...
    account = request.GET.get('account')
    psw = request.GET.get('psw')
    img = request.GET.get('img')
    if not psw:
       return resultNone('psw','') 
    if not account:
       return resultNone('account','null')
#     if isinstance(account, str):
#        return resultNone('account','not str')       
    conn = createDB()
    user = selectDB(conn,account)
    if user:
       conn.close
       return resultNone('account','uer has ') 
    addDB(conn,account,psw,img)
    conn.close
    return resultregister()