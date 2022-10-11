# __init__.py ==> 해당 파일이 포함 된 폴더 자체를 하나의 모듈로 만들어 줌(클래스와 비슷) ==>파이썬에서

# class animal():
#     def __init__(self) -> None:
#         print("동물")
#         pass
# animal()

from calculator.add import add #calculator.add 안에있는 add를 가져올 것
from calculator.diff import diff
from test4.input import testInput

# 아래와 같이 만들어준것과 흡사
# class calculator():
#     def __init__(self) -> None:
#         pass
#     def add(self,a,b):
#         return a+b
#     def diff(self,a,b):
#         return a-b

def main():
    count=0
    count=add(count,4)
    count=diff(count,10)
    print(count)
    text=testInput()
    print(text)
    
main()


class Person:
    count=0 #비공개 속성
    def __init__(self) -> None:
        Person.count+=1 #count(a), count(a)+count(b), count(a)+count(b)+count(c)
        # self.count+=1 #count(a), count(b), count(c) ==> self는 독립