# 반복문
a=["a","b","c","d","e"]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#0 <= i < len(a)
for i in range(0,len(a)) : #for는 끝이 있음(범위 필수)
    print(i)
    print(a[i])

# foreach
for i in a:
    print(i)

re = 0
while re < 5: #while은 끝을 지정하지 않을 수 있음(범위가 지정되지 않을수도)
    print(a[re])
    re+=1 #re=re+1

b=[1,2,3,4,5]
re=0
while True:
    print(b[re])
    if(b[re]%2==0):
        break #반복중지
    re+=1

for i in a:
    if i=="c":
        break
        print(i)


