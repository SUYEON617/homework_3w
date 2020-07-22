#! /usr/bin/python3m

n=int(input("수를 입력하세요 : "))

try:
    print(10/n)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
