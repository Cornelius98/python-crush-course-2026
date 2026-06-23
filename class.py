class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def walk(self):
        print(self.name, " is walking")

    def talking(self):
        print(self.name, " is talking")


Cornelius = Person("Cornelius", 10, 100)
Cornelius.walk()
Cornelius.talking()

Patson = Person("Tembo Patson", 12, 1.5)
Patson.walk()