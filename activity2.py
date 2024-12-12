# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals or vehicles with the same action (like move()). However, 
# make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while 
# Plane.move() prints "Flying" ✈️).

# class Animals:
#     def __init__(self, walkingStyle):
#         self.walkingStyle = walkingStyle
#     def move(self):
#         return f"{self.walkingStyle}"
# class Cheetah(Animals):
#     def move(self):
#         return f"A Cheetah {super().move()}"
# class Kangaroo(Animals):
#     def move(self):
#         return f"A Kangaroo {super().move()}"

# cheetah = Cheetah("runs")
# kangaroo = Kangaroo("jumps")

# print(cheetah.move())
# print(kangaroo.move())


class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "Running"

class Bird(Animal):
    def move(self):
        return "Flying"

class Fish(Animal):
    def move(self):
        return "Swimming"

class Elephant(Animal):
    def move(self):
        return "Walking slowly"

class Kangaroo(Animal):
    def move(self):
        return "Jumping"

def walkingStyle(animal: Animal):
    print(animal.move())

dog = Dog()
bird = Bird()
fish = Fish()
elephant = Elephant()
kangaroo = Kangaroo()

animals = [dog, bird, fish, elephant, kangaroo]

for i in animals:
    walkingStyle(i)
