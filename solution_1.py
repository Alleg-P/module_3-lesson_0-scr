# Задание 

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

animal1 = Animal("Dog", "Woof")
animal1.make_sound()
animal1.eat("bone")

animal2 = Animal("Cat", "Meow")
animal2.make_sound()
animal2.eat("fish")
