# 계산기 만들기
# 기본적으로

# def add(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# i=0
# i=add(i,10)
# i=diff(i,5)
# print(i)

#class
# class Calculator: #clas==>def를 모아둔 것 첫글자는 대문자로
#     def __init__(self) -> None: #init==>초기값 설정  
#         self.result=0
    
#     #@overload ==> 같은 이름의 함수가 다양한 기능을 할때 뭔가 더 필요.....
#     def add(self,b):
#         self.result+=b

#     #@overload
#     #def add(self, b, c):
#     #    self.result=self.result+b+c

#     def diff(self,b):
#         self.result-=b


# 모듈 
# from cal import Calculator #cal파일에서 Calculator를 가져옴
# from user import User 

# cal1=Calculator()             #다른 파일에서 class 가져올땐 Ctrl+SPACE
# cal1.add(10)                    
# cal1.diff(5)                   
# print(f"cal1\t{cal1.result}")

# cal2=Calculator()
# cal2.add(10)
# cal2.diff(2)
# print(f"cal2\t{cal2.result}")

# cal3=Calculator()
# cal3.add(784)
# cal3.diff(65)
# print(f"cal3\t{cal3.result}")

# user1=User("bit","1234") #=(id="bit", password="1234")
# user1.printUser()
# user1.change_id("pppp")
# user1.printUser()

# from arm import Arm
# from human import Human
# from leg import Leg

# l=Leg("left", "park")
# print(l.side)
# print(l.name)
# l.setName("kim")
# print(l.name)


from animal import Animal
from cat import Cat
from dog import Dog


# an=Animal()
# print(an.name)
# an.__setattr__("name","?") #name을 ?로
# print(an.name)
# print(an.__dict__)

# class는 하나의 물체를 만들기 위해 쓰고
# 상속은 공통 코드를 줄이기 위해서 (객체지향)
# 상속 ==> 상위 클래스의 속성을 가져다 쓸 수 있음 class B(A)==> A가 상위 클래스
# 상위 클래스의 속성을 가져다 쓰면 상위 클래스에서 해당 속성을 수정했을 때 그걸 가져다 쓴 하위 클래스에서도 수정 반영됨
cat=Cat()
cat.printSound()
print(cat.name)

dog=Dog()
dog.printSound()
print(dog.name)
print(dog.__dict__)

# #{
# 'name': '강아지', 
# 'sound': '멍멍', 
# 'master': True
# }                  ==>dog 정의
# 객체
# class는 객체지향적인 성격을 가지고 있음 class 내부 속성을 다 모아둔 것

# def run():
#     print("뛰다")
# human={"name":"park","age":46, "gender":"male","run":run()} # dict도 객체적인 속성 有
# human.get('run')
