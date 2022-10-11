class Person():
    count=0
    def __init__(self) -> None:
        Person.count+=1 #count(a), count(a)+count(b), count(a)+count(b)+count(c)
        # self.count+=1 #count(a), count(b), count(c) ==> self는 독립적

    @classmethod
    def printCount(cls): #cls=person
        print(cls.count)
    def printCount2(self): #self=c
        print(self.count)  #c.count