import requests
import re
import time
from multiprocessing import Pool

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    html = html.decode('utf-8') #python3
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
     urllib.request.urlretrieve(imgurl,'D:\E\%s.jpg' % x)
     x += 1


     def getpic(html): #获取图片地址并下载
        soup =BeautifulSoup(html,'html.parser')
        all_img=soup.find('ul',class_='pli')find_all('img')
        for img in all_img:
           src=img['src']
           img_url=src
           print (img_url)
           root='D:/pic/'
           path = root + img_url.split('/')[-1]
        print(getpic(html))