class student:
    name="sagar"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def marks(self,marks):
        self.phy=marks[0]
        self.math=marks[1]
        self.chem=marks[2]
        self.hin=marks[3]
    
    def pri(self):
        print(self.name)
        print(self.age)
        print(self.marks)
        print("percentage  :",)
        


s1=student("singh",21)
s1=student("bisht",11)

print(s1.name,s1.age)    
s1.marks(90,98,97,96)