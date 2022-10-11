# 모듈

import calendar
import math
import random
import re
import webbrowser

# print(math.pi)
# calendar.prmonth(2022,10)
# # webbrowser.open("http://naver.com")
# print(random.random()*11) #0*11<= answer*11 <1*11
# print(random.random()*11+1) #0*11+1<= answer*11 <1*11+1

# # 정규식 ==> 조건에 해당하는지 검토가 필요할 때
# # reg=re.compile("[A-z0-9]{5,15}") #[]문자
# # reg=re.compile("[0-9]") # []들어가는 첫숫자가 0-9 사이에 있으면 인정
# reg=re.compile("[0-9]{2,5}") # {}들어가는 숫자의 갯수가 2-5 사이에 있을때 인정
# id="9ㅇㄴㅁ14582"
# print(reg.match(id)) # match 첫 문자포함 조건과 정확히 일치하는 값만 찾음
# print(reg.search(id)) # search 조건에 해당하는 값이 있으면 위치 상관없이 해당되는 부분중 제일 앞부분을 찾음

# # reg=re.compile("집사")
# # print(len(reg.findall(st))) #"집사"가 몇번 나오는지  ==> 단어들을 카운트해서 자주 쓰는 단어 파악 등
# # 회원가입시 비밀번호 특수문자, 영어 대문자 포함! 이런 조건에도 활용 됨
# # e-mail 형식 검토 111@gmail.com abc@naver.com id@korea.go.kr
# reg=re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2,3})")
# print(reg.match("park@gmail.com"))

# 로또 1~45 중복없이 6개 숫자 5개 세트 번호 만들기
# random , for 활용

# for i in range(0,6):
#     lotto=[]
#     lotto.append("%d"%(random.random()*44+1))
#     print(lotto)

numbers=[]
for i in range(0,6):
    num=random.random()*45+1
    print(int(num))
    while len(numbers)<6:
        num=int(random.random()*45+1)
        tmpNumbers=numbers.copy()
        tmpNumbers.append(num) 
        setNumbers=set(numbers.copy())
        if len(setNumbers)==len(tmpNumbers):
            numbers.append(num)
print(numbers)


# reg=re.compile("([0-9]+-[0-9]{3,4}+-[A-za-z]{3,4})")
# phone_number="010-2222-3333"
# print(reg.match("phone_number"))