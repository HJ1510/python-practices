# 제어문
a=10
b=5
print(f"a>b {a>b}")
# print(f"a>b {a>b}= True 크다 False 작다)
# : 뒤에는 tab으로 무조건 띄어 쓰기
str1=""
if a>b: # 조건이 True면 아래 문장을 실행한다 
    str1="크다"
    print(f"a>b 크다")
elif a<b: 
    str1="작다"    
    print(f"a>b 작다")
else: # 위 조건들이 다 아니면 아래 문장을 실행한다
    str1="같다"    
    print(f"a=b 같다")
print(f"a>b {str1}")


c=[1,2,3,4,5]
# len(c) = 3
if len(c)>3:
    print(c[3])
if len(c)>2:
    print(c[0])
