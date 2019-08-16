"""
http://www.quanben.io/n/guantiwanzhengban/list.html

1. 开启两个进程 master, worker1
2. master 去爬取该页面的所有连接
3. worker1 爬取页面详细存入本地(可以考虑进程锁)
"""

"""
开多进程...
在2209个文件中检索关键字为"美丽,帅哥."
"""