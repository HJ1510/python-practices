# 구구단
# 2*1=2 2*2=4
# num=2
# for i in range(1,10):
#     print(f"{num}*{i}={num*i}")

# for i in range(2,10):
#     for num in range(1,10):
#         print(f"{i}*{num}={num*i}")

# 별 찍기
# *
# **
# ***
# ****
# *****
# text="*"
# for i in range(1,6):
#     print(text)

# text="*"

# for i in range(2,7):
#     st=""
#     for j in range(1,i):
#         st=text*j
#     print(st)

# 2부터 30까지 소수리스트 뽑아내기
# list1=[]
# for i in range(2,31):
#     sosu=True
#     for num in range(2,i):
#         if i%num==0:
#             sosu=False
#     if sosu:
#         list1.append(i)
# print(list1)

answer=[]
for i in range(2,31):
    isPrimary=True #소수인가? ##if i=4=>j=2,3 / i=2 2<=j<2(for문 조건에 해당x)
    #i=2, 2<= j <3
    for j in range(2,i):
        if i%j==0:
            isPrimary=False
            break
    if isPrimary:
        answer.append(i)
print(answer)



