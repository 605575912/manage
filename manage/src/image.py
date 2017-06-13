# -*- coding: utf-8 -*-
'''
Created on 2017年6月13日

@author: Administrator
'''

from django.http import FileResponse    
import os,sys
def getimage(request):  
       # do something...
    ge = request.get_full_path()
    print(ge)
    filepath_ = sys.path[0]+'\manage\\files'+ge
    response = FileResponse(open(filepath_, 'rb'), content_type='image/jpeg') 
    return response
