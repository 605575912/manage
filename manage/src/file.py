# -*- coding: utf-8 -*- 
'''
Created on 2017��6��6��

@author: Administrator
'''
from django.http import HttpResponse  
from django.http import StreamingHttpResponse 
import os,sys
import json
def myserver(request):  
       # do something...
    filepath_ = sys.path[0]+'\manage\\files\per.txt'
    print(filepath_)
    def file_iterator(file_name, chunk_size=262144):
        f = open(file_name,"rb")
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
    response = StreamingHttpResponse(file_iterator(filepath_))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(filepath_))#�趨������ͻ��˵��ļ����� 
    response['Content-Length'] = ''.format(os.path.getsize(filepath_)) #������ͻ��˵��ļ���С  
    return response