#MySQL, NoSQL, 자바, hadoop
#웹프론트 백엔드 ==> javascript, java
#머신러닝 딥러닝 텐서플로 ==> python
#MySQL, NoSQL DB

# 파이썬 
# -절차지향
# type ==> int, str, list, set, tuple, dict
# int a=1
# str a=""
# list a=[]
# set a={}
# tuple a=()
# dict a={key:value}

# 동적 타이핑
# 장점 타입을 지정 안해도 됨
# 단점 오류 발생 가능

# 스크립트 언어
# 소스코드를 한줄씩 읽어서 곧바로 실행
# python 문법으로 코드를 작성
# 기계어(컴퓨터 언어)는 이진수
# 컴파일==> python->기계어 번역
# 컴퓨터 언어로 바꿔서 따로 파일을 만들어서 그것을 실행하지 않고 바로 실행

# 플랫폼 독립적==>os 상관없음

# 제어문
# if elif else
# match case

# 반복문
# for in :
# while
# break, comtinue
# 람다 lambda ==> map, reduce, filter 
# from functools import reduce
# list1=[9,1,2,4,3]
# def sum(x,y):
#     print(f"{x} {y}") #f=format
#     return x+y
# a=reduce(lambda x,y:sum(x,y),list1)

# user={"id":"id", "pass":"pass","name":""}
# names=["kim", "lee", "park"]
# namelist=list(map(lambda x: {"id":"id", "pass":"pass","name":x},names))
# print(namelist)
# findUser=list(filter(lambda x: x.get("name")=="park", namelist))
# print(findUser)

# 함수
# def :
# def sum(a,b): a,b 매개변수
#     return a+b
# sum(1,2) 1,2 인수

# def sum(*a): *a tuple
# sum(1,2,3)
# def sum(**a): **a dict
# sum("name"="kim", "age"=30)

# name="kim" 전역변수
# def printName(name):
#     name="lee" 지역변수

# 파일입출력
# f=open(파일, mode, )
# encoding UTF-8

# 입력받고 싶을 때 ==> input

# class
# 중복되는 것 한번에 처리 객체지향
# class name(상속):
#     def __init__
#     super() ==> 상속 접근할때
#     def __init__(self) ==> self 자기자신

# import 다른 파일에서 불러올 때 사용
# import random

# 정규식
# search match 특정 조합 조건에 맞는지 확인
# import re

# C:\test -> C:\test\test2
# 상대경로
# ./test2
# .. 상위폴더
# 절대경로
# C:\test\test2
