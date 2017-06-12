# -*- coding: utf-8 -*- 
'''
Created on 2017��6��6��

@author: Administrator
'''
from django.http import HttpResponse  
import os,sys
import json
def getmine(request):  
    filepath_ = sys.path[0]+'\manage\\files\\mine_cards.txt'
    if os.path.exists(filepath_):
        f = open(filepath_, mode='r', encoding='utf-8')
        bannerjson = json.load(f)
        jsonStr = json.dumps(bannerjson) 
        print (jsonStr)
        return HttpResponse(jsonStr, content_type="application/json")  