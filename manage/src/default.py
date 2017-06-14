# -*- coding: utf-8 -*- 
'''
Created on 2017年6月6日

@author: Administrator
'''
from django.http import HttpResponse  
import json
def defalutserver(request):  
       # do something...
  #读取mongodb的文件到临时文件中  
    response_data = {}  
    response_data['result'] = 'failed'  
    response_data['message'] = 'You messed up'  
    return HttpResponse(json.dumps(response_data), content_type="application/json")    
