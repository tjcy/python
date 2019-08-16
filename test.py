from multiprocessing import Process,Queue
import os
import time

q = Queue()

def _write(q):
    print('Process(%s) is writing...' % os.getpid())
    while 1:
        time.sleep(2)
        url = 100
        q.put(url)
        print('Put %s to queue...' % url)



if __name__ == "__main__":
    p = Process(target=_write,args=(q,))
    p.start()
    p.join()

    https://www.cnblogs.com/itogo/p/5635629.html


        