from multiprocessing import Process
import multiprocessing
import csv
import pandas as pd

def _write(str_):
    print(multiprocessing.current_process().name)
    path = '\\Users\\dell\\Desktop\\ming.txt'
    with open(path, mode='a',encoding='gbk') as f:
        with open('C:\\Users\\dell\\Desktop\\un-general-debates.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            column1 = [row[1]for row in reader]
            print(column1)
        f.write(str_)
if __name__ == "__main__":
    ming = pd.read_csv('C:\\Users\\dell\\Desktop\\un-general-debates.csv', usecols=['session', 'year', 'country'],nrows=3)
    print(ming)
    #wenzi = pd.read_csv('C:\\Users\\dell\\Desktop\\un-general-debates.csv', usecols=['text',],nrows=3)
    #print(wenzi)
    p1 = Process(target=_write,args=('ming\n',))
    #p2 = Process(target=_write,args=('wenzi\n',))
    p1.start()
    #p2.start()
    p1.join()
    #p2.join()