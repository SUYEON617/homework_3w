#! /usr/bin/python3m
n=int(input("숫자를 입력하세요 :"))

def fac(n):
    first=1
    for i in range(1,n+1):
        first*=i
    print(first)

fac(n)
