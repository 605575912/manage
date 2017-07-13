# -*- coding: utf-8 -*-
'''
Created on 2017年6月13日

@author: Administrator
'''

from django.http import FileResponse    
import os,sys
from django.http import HttpResponse  
from os.path import getsize
def getmusic(request):  
       # do something...
    ge = request.get_full_path()
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    print(ua)
    rangea = request.META.get('HTTP_RANGE', 'unknown')
    print(rangea)
    print(ge)
    
    filepath_ = sys.path[0]+'\manage\\files'+ge
    
#     response = FileResponse(open(filepath_, 'rb'), content_type='audio/mp3') 
    def readFile(fn, buf_size=2144):
        f = open(fn, "rb")
        f.seek(1024*1024,0)
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()
 
    response = HttpResponse(readFile(filepath_))
    response['Content-Length'] = getsize(filepath_)
    response['Content-Type'] = 'audio/mp3'  
#     
#     down_link = '' #下载链接  
#     file_size = 271768736 #文件总大小  
# 
#     while True:  
#         lsize = get_local_file_exists_size(filepath_)  
#         if lsize == file_size:  
#             break  
#         webPage = get_file_obj(request,down_link, lsize)  
#         try:  
#             file_obj = open(filepath_, 'ab+')  
#         except Exception as e:  
#             print (u"打开文件:%s失败" % filepath_)  
#             break  
#         try:  
#             for chunk in webPage.iter_content(chunk_size=64 * 1024):  
#                 if chunk:  
#                     file_obj.write(chunk)  
#                 else:  
#                     break  
#         except Exception as e:  
#             time.sleep(5)  
#         file_obj.close()  
#     response = HttpResponse(file_obj, content_type='audio/mp3') 
#         webPage.close() 
    return response

import time  
  
  
def get_local_file_exists_size(local_path):  
    try:  
        lsize = os.stat(local_path).st_size  
    except:  
        lsize = 0  
    return lsize  
  
  
def get_file_obj(requests,down_link, offset):  
    webPage = None  
    try:  
        headers = {'Range': 'bytes=%d-' % offset}  
        webPage = requests.get(down_link, stream=True, headers=headers, timeout=120, verify=False)  
        status_code = webPage.status_code  
        if status_code in [200, 206]:  
            webPage = webPage  
        elif status_code == 416:  
            print (u"%s文件数据请求区间错误,status_code:%s" % (down_link, status_code))  
        else:  
            print (u"%s链接有误,status_code:%s" % (down_link, status_code))  
    except Exception as e:  
        print (u"无法链接:%s,e:%s" % (down_link, e))  
    finally:  
        return webPage  
  
  
  
