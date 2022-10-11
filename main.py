#main 내가 실행시킬것
#java는 무조건 main start

#pakage 묶음
from calC import Calc
from calculator.add import add
from calculator.diff import diff
from test4.input import testInput
from user.age import showAge
from user.name import showName
from person import Person


def main():
    count=0
    count=add(count,4)
    count=diff(count,10)
    print(count)
    # text=testInput()
    # print(text)
    # showName("park")
    # showAge(21)
    # a=Person()
    # b=Person()
    c=Person()
    # print(a.count)
    # print(b.count)
    # print(c.count)
    Calc.add(1,3)
    Calc.diff(1,3)
    Calc.diff(1,2)
    print(c.count)
    print(c.printCount)
    print(c.printCount2)
    
main()