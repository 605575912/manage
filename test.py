# -*- coding: gbk -*- 
'''

@author: Administrator
'''
import os,sys
import json
from django.http import HttpResponse 
filepath_ = os.path.abspath('.')+'\manage\\files\per.txt'
# print (sys.(filepath_))
 
  
response_data = {}  
response_data['result'] = 'failed'  
response_data['message'] = 'You messed up'  
return HttpResponse(json.dumps(response_data), content_type="application/json") 

print(filepath_)
print (os.path.exists(filepath_))
print (os.path.getsize(filepath_))
