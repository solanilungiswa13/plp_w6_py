class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        print("Running")


class Bird(Animal):
    def move(self):
        print("Flying")


class Snake(Animal):
    def move(self):
        print("Slithering")


# Example usage
animals = [Dog(), Bird(), Snake()]
for animal in animals:
    animal.move()