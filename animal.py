class Animal:
    def __init__(self) -> None:
        self.name="sss"
        self.sound=""
        
    def setName(self,name):
        self.name=name

    def setSound(self, sound):
        self.sound=sound
    
    def printSound(self):
        print(self.sound)