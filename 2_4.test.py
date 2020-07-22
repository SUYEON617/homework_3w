#! /usr/bin/python3m

import sys
import json

def read_csv(file_name):
    with open(file_name,'r') as k:
        ret=[]
        for line in k:
            if line.startswith("sample"):
                sam=line.strip().split(',')
                continue
            su=line.strip().split(',')
            d=dict(zip(sam,su))
            for x in sam:
                d[x]=float(d[x])
            ret.append(d)
    return ret

def to_json(l,file_name):
    with open(file_name,"w") as kk:
        json.dump(l,kk,indent=4)

if __name__=="__main__":
#    if len(sys.argv) !=2:
#        print(f"#usage : python {sys.argv[0]} [csv]")
#        sys.exit()
    file_name=sys.argv[1]
    ret=read_csv(file_name)
    new_file_name=sys.argv[2]
    to_json(ret,new_file_name)
