#! /usr/bin/python3m

import json

class Abc():
    def __init__(self,filename):
        self.filename=filename
        self.dic={}
    def read_csv(self):
        ret=[]
        with open(self.filename,'r') as ff:
            for line in ff.readlines():
                k=line.strip().split(',')
                ret.append(k)
            d=dict(zip(ret[0],ret[1]))
            for x in d[ret[0]]:
                d[x]=float(d[x])
        print(d)

t=Abc('example.csv')
d=t.read_csv()

