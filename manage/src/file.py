# -*- coding: utf-8 -*- 
'''
Created on 2017��6��6��

@author: Administrator
'''
from django.http import HttpResponse  
import os,sys
import json
def myserver(request):  
       # do something...
#     filepath_ = sys.path[0]+'\manage\\files\per.txt'
#     print(filepath_)
#     def file_iterator(file_name, chunk_size=262144):
#         f = open(file_name,"rb")
#         while True:
#              c = f.read(chunk_size)
#              if c:
#                  yield c
#              else:
#                  break
#         f.close()
#     if not os.path.exists(filepath_):   
#       response_data = {}  
#       response_data['result'] = 'failed'  
#       response_data['message'] = 'You messed up'  
#       return HttpResponse(json.dumps(response_data), content_type="application/json")    
#     response = StreamingHttpResponse(file_iterator(filepath_))
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(filepath_))#�趨������ͻ��˵��ļ����� 
#     response['Content-Length'] = ''.format(os.path.getsize(filepath_)) #������ͻ��˵��ļ���С  
#     return response
    filepath_ = sys.path[0]+'\manage\\files\\banners.txt'
    home_cardsfilepath_ = sys.path[0]+'\manage\\files\\home_cards.txt'
    columndata = sys.path[0]+'\manage\\files\\columndata.txt'
    discounttxt= sys.path[0]+'\manage\\files\\discount.txt'
    itempath = sys.path[0]+'\manage\\files\\items.txt'
    if os.path.exists(filepath_):
        card={}
        cards=[]
        #banners
        f = open(filepath_, mode='r', encoding='utf-8')
        bannerjson = json.load(f)
        cards.append(bannerjson)
        
        colum = open(columndata, mode='r', encoding='utf-8')
        columjson = json.load(colum)
        cards.append(columjson)
        
        discountdata = open(discounttxt, mode='r', encoding='utf-8')
        discountjson = json.load(discountdata)
        cards.append(discountjson)
        home_cards = open(home_cardsfilepath_, mode='r', encoding='utf-8')
        home_cardsjson = json.load(home_cards)
        cards.append(home_cardsjson)
        card["cards"]=cards
        
        
        itemtxt = open(itempath, mode='r', encoding='utf-8')
        itemjson = json.load(itemtxt)
#         items=[]
#         items.append(itemjson)  
        card["items"]=itemjson
        card["titletype"] =1 
        jsonStr = json.dumps(card) 
        return HttpResponse(jsonStr, content_type="application/json")  