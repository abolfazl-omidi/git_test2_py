class Person :
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")

odis = Person('abol' , 18)
odis.eat()