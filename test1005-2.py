#함수
#def=define
#return 반환
#파이썬은 절차 지향 vs.자바는 객체 지향(OPP)
#isPrimary=True cammel case / is_primary=True snake case 회사마다 주로 사용하는 것이 다름
#(is구문은 보통 bool형에 씀)
# 기본 내장 함수 print / .append / .get 등

# def sum(a,b):   #a,b 매개변수
#     return a+b
# print(sum(1,2))    #1,2 인수

# def sum1(*args): #argument 매개변수 * 튜플 인수 여러개 입력 가능
#     print(args)
#     pppp=0
#     for arg in args:
#         pppp+=arg
#     return pppp
# print(sum1(1,1,1,1))
# print(sum1(1,2,3))


# def printFunc(**kwargs): #** 딕셔너리 인수 여러개 입력 가능
#     print(kwargs)
# printFunc(a=1,b=1)

# def makeHuman(name, age):
#     return{"name":name, "age":age}
# human1=makeHuman("kim", 30)
# human2=makeHuman("park", 34)
# print(human1)
# print(human2)



# def isPrimaryNumber(num):
#     isPrimary=True
#     for j in range(2,num):
#         if num%j==0:
#                 isPrimary=False
#                 break
#     if isPrimary:
#         return f"{num}은 소수입니다"
#     else:
#         return f"{num}은 소수가 아닙니다"

# print(isPrimaryNumber(7))


# def isPrimaryNumbers(*nums): #튜플(*) 구성시 구성인수를 하나하나 빼와야하기때문에 for 필요
#     for num in nums:
#         isPrimary=True
#         for j in range(2,num):
#             if num%j==0:
#                     isPrimary=False
#                     break
#         if isPrimary:
#             print(f"{num}은 소수입니다")
#         else:
#             print(f"{num}은 소수가 아닙니다")

# isPrimaryNumbers(9,4,2,11,16)
# print(isPrimaryNumbers(9,4,2,11,16)) #마지막 none은 반환값이 없기때문에

# def ooo(a):
#     print(a)
#     return "hello"
# print(ooo("hi"))

# def ooo(a):
#     print(a)
# print(ooo("hi"))

# def ooo(a):
#     print(a)
#     return""
# print(ooo("hi"))

# name="park"
# def setName1(name):
#     print(name)
#     name=name
#     print(name)
# print(name)
# setName1("kim")
# print(name)


name="park" #전역변수(함수 밖) vs지역변수(함수 안에서만)
name1="lee" #전역변수
def setName1(name): #매개변수
    print(f"2.{name}") #kim
    #name1=name
    name=name #지역변수
    print(f"3.{name} {name1}") #kim
setName1("kim") #인자값
print(f"1.name1:{name1}") #1.name1:
print(f"1.{name}") #park
print(f"4.{name}") #park
print(f"2.name1:{name1}") #2.name1:
setName1("yoon") #인자값


# name="park" #전역변수(함수 밖)
# name1="lee" #전역변수
# def setName1(name): #매개변수
#     print(f"2.{name}")
#     print(f"3.{name} {name1}")
# setName1("yoon")




