# -*- coding: utf-8 -*- 
'''
Created on 2017年6月8日

@author: Administrator
'''
from django.http import HttpResponse  
from django.http import StreamingHttpResponse 
import os,sys
import json
def tabs(request):  
       # do something...
    filepath_ = sys.path[0]+'\manage\\files\\tabs.txt'
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
