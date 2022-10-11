# from re import S


# print("%d/%d=%0.1f"%(100,200,0.5))

# a="만세"
# a
# print(a)
# a= "그는 \"안녕\"이라고 말했다"
# print(a)

# a="""안녕
# 하세여"""
# print(a)

# def myFunc():
#     print('함수 시작')
# b=30
# def main():
#     print('함수 실행')
#     myFunc()
#     print('변수값', b)

# if __name__=="__main__":
#     main()

# money,c500,c100,c50,c10=0,0,0,0,0
# money=int(input("교환할 돈은 얼마?"))
# c500=money//500




# def evenOrOdd(num):
#     return["Even", "Odd"][num&1]
# print(evenOrOdd(3))


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

# i=0
# while True:
#     i+=1
#     myInput=input(f"현재값 {i}")
#     print(myInput)
#     if myInput != str(i+1):
#         print("틀렸어")
#     else:
#         print("맞았어")



# i=0
# while True:
#     i+=1
#     myInput=input(f"현재값 {i}")
#     print(myInput)
#     if myInput != str(i+1):
#         print("x")
#     else:
#         print("pass")

# def game():
#     i=0
#     while True:
#         i+1
#         myInput=input(f"현재값 {i}")
#         answer=str(i+1)
#         for c in str(i+1):
#             if c=="3" or c=="6" or c=="9":
#                 answer="c"
#         if myInput==answer:
#             print("pass")
#         else:
#             print("game over")
#             break


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

