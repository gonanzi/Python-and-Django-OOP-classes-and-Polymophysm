#Activity 2: Python Program: Polymorphism with move() Method

# Base class for animals
class Animal:
    def move(self):
        pass

# Dog class inherits from Animal
class Dog(Animal):
    def move(self):
        print("Running")

# Cat class inherits from Animal
class Cat(Animal):
    def move(self):
        print("Sneaking")

# Bird class inherits from Animal
class Bird(Animal):
    def move(self):
        print("Flying")

# Base class for vehicles
class Vehicle:
    def move(self):
        pass

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Boat class inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Main function to demonstrate polymorphism
def main():
    # instances of different animals and vehicles
    dog = Dog()
    cat = Cat()
    bird = Bird()
    car = Car()
    plane = Plane()
    boat = Boat()

    # Listing objects to demonstrate polymorphism
    movers = [dog, cat, bird, car, plane, boat]

    # Looping through each object and call the move method
    for mover in movers:
        mover.move()

# Run the main function
if __name__ == "__main__":
    main()
