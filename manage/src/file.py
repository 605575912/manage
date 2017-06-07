# -*- coding: gbk -*- 
'''
Created on 2017年6月6日

@author: Administrator
'''
from django.http import HttpResponse  
from django.http import StreamingHttpResponse 
import os,sys
def myserver(request):  
       # do something...
  #读取mongodb的文件到临时文件中  
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
    response = StreamingHttpResponse(file_iterator(filepath_))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="d"'#设定传输给客户端的文件名称 
    response['Content-Length'] = ''.format(os.path.getsize(filepath_)) #传输给客户端的文件大小  
    return response