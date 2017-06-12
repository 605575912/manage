#coding=utf-8
'''
Created on 2017��6��12��

@author: Administrator
'''
import json
from django.http import HttpResponse  
def resultNone(data,msg):#失败提示
    response_data = {}  
    response_data['result'] = 0  
    response_data[data] = msg  
    return HttpResponse(json.dumps(response_data), content_type="application/json")
def resultLogin(token,user):#登录
    response_data = {} 
    response_data['result'] = 1
#     response_data['token'] = token
    user["token"]=(not token )and token or ''
    response_data['user'] = user    
    return HttpResponse(json.dumps(response_data), content_type="application/json")
def resultregister():#注册
    response_data = {}  
    response_data['result'] = 1
    return HttpResponse(json.dumps(response_data), content_type="application/json")  