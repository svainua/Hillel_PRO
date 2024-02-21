from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Pet):
    def sound(self):
        print("Gav Gav")


class Cat(Pet):
    def sound(self):
        print("Miau")


def foo(pet: Pet):
    pet.sound()


joe = Dog()
foo(joe)

tom = Cat()
foo(tom)
