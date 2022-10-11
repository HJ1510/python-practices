# #반복문
# #for while

# for i in range(0,3): # 0<= i <3
#     print(i)

# list1=["a", "b", "c"]
# for i in range(0, len(list1)):
#     print(list1[i])
# for element in list1:
#     print(element)


# index=0
# while index < len(list1): # while index < 3
#     print(list1[index])
#     index+=1

# #break continue
# #list1=[9,4,2,1,6,7,5,4,3,7]
# #만약에 홀수면 2배, 짝수면 그냥(list3) / list1의 숫자 기준 합이 20이 넘으면 끝

# list1=[9,4,2,1,6,7,5,4,3,7]
# list2=[]
# list3=[]
# list4=[]

# i=0
# sum1=0
# while i<len(list1):
#     sum1 += list1[i] 
#     # sum1=sum1+list1[i] 
#     # i=0, sum1=0, list1[i]=9 
#     # i=1, sum1=9, list[i]=4 
#     # i=2, sum1=13, list[i]=2
#     # i=3, sum1=15, list[i]=1
#     # i=4, sum1=16, list[i]=6
#     # i=5, sum5=22, list[i]=7
#     if list1[i]%2==1:
#         list2.append(list1[i]*2)
#     elif list1[i]%2==0:
#         list2.append(list1[i])
#     i+=1
#     if sum1>20 :
#         break
# print(list2)

# i=0
# sum1=0
# while i<len(list1):
#     sum1 += list1[i] 
#     if list1[i]%2==1:
#         list4.append(list1[i]*2)
#     elif list1[i]%2==0:
#         list4.append(list1[i])
#     i+=1
#     if sum1>20 :
#         continue
#     print("end")
# print(list4)

# for i in range(0,len(list1)):
#     if list1[i]%2==1:
#         list3.append(list1[i]*2)
#     elif list1[i]%2==0:
#         list3.append(list1[i])
# print(list3)

from turtle import hideturtle
from xml.dom.minidom import Element


list1=["안", "녕", "하", "세", "요"]

index=0
hi=""
while index<len(list1):
    #index=0, hi=""
    print(hi)
    hi+=list1[index]
    #index=0, hi="안"
    print(hi)
    index+=1
    #index=1, hi="안"
print(hi)    

for index in range(0, len(list1)):
    hi+=list1[index]
print(hi)

for element in list1:
    hi=hi+element 
print(hi)


x = {"company":"카카오", "isPartTime": False}
for element in x:
    print(element)
print(x["isPartTime"])    

tup=(1,2,3)    
for element in tup:
    print(element)

# num=5
# for element in num:
#     print(element)

st="안녕하세요"    
for element in st:
    print(element)
