class Preson():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printInfo(self):
        print(self.name,self.age,sep=',')
name=input()
age=input()
preson=Preson(name,age)
preson.printInfo()

