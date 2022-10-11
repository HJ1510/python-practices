# 1 자연수 뒤집어 배열
# 2 제일 작은 수 제거하기
# 3 두 정수 사이의 합
# 4 정수 제곱근 판별 *


# def solution(n):
#     answer=0
#     for x in range(1,n+1):
#         if n==x**2:
#             answer=(x+1)**2
#             break
#         else:
#             answer=-1
#     return answer
# print(solution(1))

##1?
# def solution(n):
#     for x in range(1,n+1):
#         if n==x**2:
#             return (x+1)**2
#             break
#         else:
#             return -1
# print(solution(16))

##2?
# def solution(n):
#     answer=0
#     for x in range(1,n+1):
#         if n==x**2:
#             answer=(x+1)**2
#         else:
#             answer=-1
#     return answer
# print(solution(4))

##2
# def solution(n):
#     answer=0
#     for x in range(1,n+1):
#         if x*x==n:
#             answer=x
#             break
#     if answer==0:
#         return -1
#     return (answer+1)*(answer+1)
# print(solution(2))

##3
# def solution(n):
#     answer=0
#     for x in range(1,n+1):
#         if x*x==n:
#             answer=(x+1)**2
#             break
#         elif x**2>n:   #큰 숫자일 때 속도증가
#             break
#     if answer==0:
#         return -1
#     return answer
# print(solution(169))

##4

# # 2 제일 작은 수 제거하기 *
# def solution(arr):
#     answer = []
#     if len(arr)==1:
#         return [-1]
#     #제일 작은 수
#     minNumber=1000000
#     for a in arr:
#         if a < minNumber:
#             minNumber=a
#     #제거하기
#     arr.remove(minNumber)
#     # for a in arr:
#     #     if minNumber!=a:
#     #         answer.append(a) ==> return answer
#     return arr
# print(solution([10]))
# print(solution([4,3,2,1]))

# # 3 두 정수 사이의 합
##1
# def solution(a, b):
#     answer = 0
#     if a==b:
#         answer=a
#     elif a>b:
#         for i in range(b, a+1):
#             answer+=i
#     else:
#         for i in range(a, b+1):
#             answer+=i
#     return answer
# print(solution(1,10))
##2
# def solution(a,b):
#     answer=0
#     if b>a:
#         list1=list(range(a,b+1))
#         answer=sum(list1)
#     elif a<b:
#         list1=list(range(b,a+1))
#         answer=sum(list1)
#     else:
#         answer=a
#     return answer
# print(solution(1,10))
##3
# def solution(a,b):
#     answer=0
#     if b>a:
#         return sum(range(a,b+1))
#     elif a<b:
#         return sum(range(b,a+1))
#     else:
#         answer=a
#     return answer
# print(solution(1,10))


# # 1 자연수 뒤집어 배열
# def solution(n):
#     answer = []
#     n=str(n)
#     answer=list(n)
#     answer.reverse()
#     for el in range(0,len(answer)):
#         answer[el]=int(answer[el])    
#     return answer
# print(solution(56789))
##2
# def solution(n):
#     answer = []
#     answer=list(str(n))
#     answer.reverse()
#     for el in range(0,len(answer)):
#         answer[el]=int(answer[el])    
#     return answer
# print(solution(56789))
# #3
# def solution(n):
#     answer=[]
#     n=list(str(n))
#     for i in range(len(n),0,-1): #range(10,0,-1) 10부터 0까지 역순으로
#         answer.append(int(n[i-1]))    
#     return answer
# print(solution(56789))

#피보나치 수
# F(0)=0, F(1)=1
# F(n)=F(n-1)+F(n-2)
# F(2)=F(1)+F(0)=1+0=1
# F(3)=F(2)+F(1)=1+1=2
# F(4)=F(3)+F(2)=2+1=3
# F(5)=F(4)+F(3)=3+2=5
# F(6)=F(5)+F(4)=5+3=8
# def solution(n):
#     i=[0,1]
#     print(i)
#     i[n]=i[n-1]+i[n-2]
# n=2
# i=[0,1]
# print(i)
# for n in range(2,n+1):
#     i.append(int(n))
#     print(i)
# i[n]=i[n-1]+i[n-2]
# print(i)


def solution(n:int): #n:int 타입지정
    answer=1     # F(2)=F(1)+F(0)=1+0=1 ==> 이것을 세줄로 설명
    first=0
    second=1
    for i in range(2,n+1):
        answer=first+second #0+1
        first=second
        second=answer
    return answer%1234567
print(solution(120))