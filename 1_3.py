#! /usr/bin/python3m

a=input("염기 한 글자를 입력하세요 : ")
def base(a):
    a=a.upper()
    d={'A':'Adenine','T':'Thymine','C':'Cytosine','G':'Guanine','U':'Uracil'}
    print(d[a])
base(a)
