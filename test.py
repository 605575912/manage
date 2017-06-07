# -*- coding: gbk -*- 
'''

@author: Administrator
'''
import os,sys
import json

filepath_ = os.path.abspath('.')+'\manage\\files\per.txt'
# print (sys.(filepath_))
 
  

print(filepath_)
print (os.path.exists(filepath_))
print ('{}'.format(os.path.basename(filepath_)))
