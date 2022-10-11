#정적 ==> 변화가 없다

from typing import overload

class Calc:
    count=0
    @staticmethod  #@는 어노테이션 slef->any로 바꿔줌, 선언 필요 없어짐
    def add(a,b):
        print(a+b)
    @staticmethod
    # @overload  #같은 이름으로 다른갯수의 인수를 활용하거나 동작이 다름
    def diff(s,a,b):
        print("diff 3개짜리")
    @staticmethod
    # @overload
    def diff(s,a):
        print("diff 2개짜리")
