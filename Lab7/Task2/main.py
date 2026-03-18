
from models import Animal, Dog, Bird


def main():
    animal = Animal("Generic", 5, "Forest")
    dog = Dog("Rex", 3, "House", "Labrador")
    bird = Bird("Sky", 2, "Jungle", True)

    animals = [animal, dog, bird]

    for a in animals:
        print(a)
        print(a.speak())
        print(a.move())
        print()

    print(dog.fetch())
    print(bird.fly())


if __name__ == "__main__":
    main()