#코딩테스트 (1. 백준(난이도 上), 2. 프로그래머스)

# def solution(num):
#     for i in range(1,num):
#         if num%2==0:
#             return "Even"
#         elif num%2==1:
#             return "Odd"

# def solution(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return"Odd"

# solution(3)

# print(solution(3))
# print(solution(4))

# a=input("입력하세요")
# print(a)

# def sum(a,b):
#     return a+b #return한 순간 함수는 종결 그 뒤에 무엇이 와도 진행x
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))

# def sum(c,d):
#     return c+d
# c = int(input("입력하세요"))
# d = int(input("입력하세요"))
# print(sum(c,d))

#형변환
# def sum(a,b):
#     print(type(a))
#     if type(a)==int and type(b)==int:
#         return a+b
#     else:
#         return int(a)+int(b)
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))

# def sum(a,b):
#     try:
#         if type(a)==int and type(b)==int:
#             return a+b
#         else:
#             return int(a)+int(b)
#     except: #파이썬에서 except지만 다른데서는 catch를 주로 사용
#         return f"{a}랑 {b} 중 숫자가 아닌게 있습니다."
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))


# while True:
#     a = input("입력하세요")
#     if a=="end":
#         break
#     b = input("입력하세요")
#     if b=="end":
#         break
#     print(sum(a,b))

# for i in range(0,10):
#     a = input("입력하세요")
#     if a=="end":
#         break
#     b = input("입력하세요")
#     if b=="end":
#         break
#     print(sum(a,b))

# 3,6,9게임
# 다음 숫자에 3,6,9가 있으면 c
# 지속되어야하는 게임
# 369369 현재 {i}
# 입력 다음 할 것

# def game(i):
#     try:
#         if int(i)=="6":
#             return f"369369 현재 {i} {i+1}"
#         else:
#             return f"369369 현재 {i} c"

#     except:
#         return "졌습니다."

# print(game(7))


# while True:
#     if game(i)=="졌습니다":
#         break

# i=0
# while True:
#     i+=1
#     myInput=input(f"현재값 {i}")
#     print(myInput)
#     if myInput != str(i+1):
#         print("틀렸어")
#     else:
#         print("맞았어")
# def game():
#     i=0
#     while True:
#         i+=1
#         myInput=input(f"현재값 {i}")
#         answer=str(i+1)
#         for c in str(i+1):
#             if c=="3" or c=="6" or c=="9":
#                 answer="c"
#         if myInput==answer:
#             print("맞았다")
#         else:
#             print("game over")
#             break



# for c in str(123456):
#     print(c)

# def game(cur, myInput):
#     answer=str(cur+1)
#     for c in str(cur+1):
#         if c=="3" or c=="6" or c=="9":
#             answer="c"
#     if myInput==answer:
#         print("맞았다")
#         return True
#     else:
#         print("game over")
#         return False

# i=0
# while True:
#     i+=1
#     myInput=input(f"현재 값 {i}")
#     isWin=game(i,myInput)
#     if(not isWin):
#         break

def solution(phone_number):
    answer = ''
    len=len(phone_number)
    answer="*"*(len-4)
    answer+=phone_number[-4:]
    return answer
print(solution("01033334444"))
print(solution("027778888"))

#뒤 4자리만 빼고 다 *
#input 번호 받아서 010-0000-0000
