class Animal:
    def __init__(self, name, age, area):
        self.name = name
        self.age = age
        self.area = area

    def speak(self):
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} moves around"

    def __str__(self):
        return f"Animal(Name: {self.name}, Age: {self.age}, Area: {self.area})"



class Dog(Animal):
    def __init__(self, name, age, area, breed):
        super().__init__(name, age, area)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching a stick"

    def __str__(self):
        return f"Dog(Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Area: {self.area})"



class Bird(Animal):
    def __init__(self, name, age, area, can_fly):
        super().__init__(name, age, area)
        self.can_fly = can_fly

    def speak(self):
        return "Chirp!"

    def fly(self):
        return f"{self.name} is flying" if self.can_fly else f"{self.name} cannot fly"

    def __str__(self):
        return f"Bird(Name: {self.name}, Can Fly: {self.can_fly}, Age: {self.age}, Area: {self.area})"