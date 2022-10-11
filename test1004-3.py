# list = [1,2,3,4,5,6,2,3,5,1]
# 뭐는 짝수입니다.
# 뭐는 홀수입니다.

from functools import reduce

list1=[1,2,3,4,5,6,2,3,5,1]


for el in list1:
    if el % 2==0:
        print(f"{el}은 짝수입니다")
    elif el % 2==1:
        print(f'{el}은 홀수입니다')



i=0
while i<len(list1):
    if list1[i]%2==0:
        print(f"{list1[i]}은 짝수입니다") 
    elif list1[i]%2==1:
        print(f"{list1[i]}은 홀수입니다") 
    i+=1

i=0
while i<len(list1):
    if list1[i]%2==0:
        print(f"{list1[i]}은 짝수입니다") 
    elif list1[i]%2==1:
        print(f"{list1[i]}은 홀수입니다") 
    i+=1



list1=[1,2,3,4,5,6,2,3,5,1]


for el in list1:
    match el %2:
        case 1:
            print(f"{el}은 홀수입니다")
        case 0:
            print(f"{el}은 짝수입니다")            

    # #if el%2==0:
    #     print(f"{el}은 짝수입니다")
    # elif el%2==1:
    #     print(f"{el}은 홀수입니다")


# 람다 버전 3.6부터
# 예제 list1의 요소를 *2해서 찍어봐라

list1=[1,2,3,4,5,6,2,3,5,1]

# list1 요소의 합? int(수)
sum = 0
for el in list1:
    sum = sum+el
    # sum+=el
print(sum)    

sum2=reduce(lambda x,y:x+y, list1)
# 합계 구할 때
print(sum2)


list2=[]
for el in list1:
    list2.append(el*2)
print(list2)

list3=[]
for el in range(0, len(list1)):
    list3.append(list1[el]*2)
print(list3)

# map은 새로운 리스트를 만든다 (반환한다)
list4=list(map(lambda el:el**2, list1))
print(list4)


tmpd={"name":"re", "age":100}
list5=[tmpd, tmpd, tmpd]
list6= list(map(lambda el: el.copy(), list5)) # [tmpd.copy(), tmpd.copy(), tmpd.copy()]
list7=list5.copy() # [tmpd, tmpd, tmpd]
print(list5)
print(list6)
print(list7)
list5.append(1)
print()
print(list5)
print(list6)
print(list7)
tmpd["age"]=10
print()
print(list5)
print(list6)
print(list7)


list1=[1,2,3,4,5,6,2,3,5,1]
# 4 이상인 것만 리스트를 만든다
list0=[]
for el in list1: #in list1 리스트 길이만큼
    # print(el)
    if el>=4 :
        list0.append(el)
print(list0)

list01=list(filter(lambda x:x>=4, list1))
print(list01)