from multiprocessing import Process
from random import randint
from time import time, sleep
import os,re
import requests
import urllib.request


def download_task(start,end):
    for i in range(1,2):
        url = 'http://op.hanhande.net/shtml/op_wz/list_2602_%d.shtml'%i
        response = requests.get(url)
        response.encoding = 'gbk'
        HTML = response.text
        #print(response.status_code)
        #print(url)
        
        links = re.findall(HTML)
        for link in links:
            pic = requests.get(link,HTML)
            pic_name = re.search('(?<=dl=).*\.jpg', link).group()
        with open('C:/Users/YangYu/Desktop/haiziewang/' + pic_name, mode='wb') as pf:
            pf.write(pic.content)
        print("完成图片下载:" + pic_name)
    
        # reg = re.compile(r'<img src="(.*?)"/>', re.S)   
        # imgre = re.compile(reg)     
        
        # imglist = re.findall(imgre,HTML)     
    
        # x = 0
        # print(reg)
        # for imgurl in imglist:
        #     urllib.request.urlretrieve(imgurl,r'C:\Users\YangYu\Desktop\haiziewang\%s.jpg' % x)
        #     x += 1
        #     print(x)

def main():
    start = time()
# 开启两个多进程，     函数名              传递的参数,需要注意的是,它接受的是一个元组(tuple)
    p1 = Process(target=download_task, args=(1,15))
    p2 = Process(target=download_task, args=(15,28))


# 启动进程
    p1.start()
    p2.start()

##############
# 进程阻塞.
    p1.join()
    p2.join()
##############
    end = time()
    print('总共用时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()