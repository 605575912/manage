#coding=utf-8
'''

@author: Administrator
'''
import re
import urllib.request  
import json
import time
import os,sys
# response = urllib.request.urlopen('http://www.fruitday.com/?tracking=PgwM0g237Q')  
# html = response.read()
# print(html) 
req = urllib.request.Request('http://www.fruitday.com/')  
response = urllib.request.urlopen(req)  
the_page = response.read()
the_page=the_page.decode('utf-8')
# print(the_page)  
# reg = r".*<section(.*)findall.*"
# reg = r'<section[^>]+>'
# imgre = re.compile(reg)
# imglist = re.findall(imgre,the_page)
# print(imglist)
  
def getbanner(the_page):
    html_script = r'p-component-banner(.*?)</section>'  
    m_script = re.findall(html_script,the_page,re.S|re.M)
# print(m_script)
    for script in m_script:  
        res_original = r'<a href="(.*?)\)"' #原图  
        m_original = re.findall(res_original,script)
        banners={} 
        list=[]   
        for pic_url in m_original:  
#             print (pic_url)
            res_jumpcontent = r'(http.*?)" ' #原图  
            m_jumpcontent = re.findall(res_jumpcontent,pic_url,re.M)
#             print (m_jumpcontent[0])
            res_img = r'url\((.?.*)' #图片 
            m_img = re.findall(res_img,pic_url)
#             strinfo = re.compile('https')
#             b = strinfo.sub('http',m_img[0])
#             print (m_img[0])
            data={} 
            data["id"]=1  
            data["imgurl"]=m_img[0]  
            data["jumpcontent"]=m_jumpcontent[0]  
            data["starttime"]= (round(time.time()*1000))
            list.append(data)
        banners["banners"]=list     
        jsonStr = json.dumps(banners) 
        print (jsonStr)
        file_object = open('files/banners.txt', 'w')
        file_object.write(jsonStr)
        file_object.close( )
#只输出一个URL 否则输出两个相同的URL
getbanner(the_page)

# html_script = r'url\((.?.*)'  
# m_script = re.findall(html_script,"http://awshuodong.fruitday.com/sale/blueBerry1706/index.html?region_id=106092\" style=\"background-image:url(https://imgjd3.fruitday.com/images/2017-06-08/9ccb2bcf569412e733570ef949fec618.jpg",re.S|re.M)
# print (m_script)
