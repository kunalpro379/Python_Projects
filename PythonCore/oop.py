#single inheritance
class Animal:
    def sound(self):
        print ("animal sound")
class Dog(Animal):
    def sound(self):
        print ("bark")
    
dog=Dog()
dog.sound()
# Output: bark

#multiple inheritance
class A:
    def methodA(self):
        print("A method")
class B:
    def methodB(self):
        print("B method")
#child class inheriting from multiple parent classes 
class C(A, B):
    pass
#create object of child class
c = C()
c.methodA()
c.methodB()
# Output: A method

#Multilevel inheritance

class A:#grand parent class 
    def methodA(self):
        print("A method")
#parent class inheriting from class A
class B(A):
    def methodB(self):
        print("B method")
class C(B):#child class inheriting from class B
    def methodC(self):
        print("C method")
#create object of child class
c = C()
c.methodA()
c.methodB()
c.methodC()


