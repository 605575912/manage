# -*- coding: gbk -*- 
'''
Created on 2017��6��6��

@author: Administrator
'''
from django.http import HttpResponse  
import json
def defalutserver(request):  
       # do something...
  #��ȡmongodb���ļ�����ʱ�ļ���  
    response_data = {}  
    response_data['result'] = 'failed'  
    response_data['message'] = 'You messed up'  
    return HttpResponse(json.dumps(response_data), content_type="application/json")    
