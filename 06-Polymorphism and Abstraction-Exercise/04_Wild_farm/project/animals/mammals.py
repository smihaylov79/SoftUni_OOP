from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):

    @property
    def weight_increment(self):
        return 0.1

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    @property
    def weight_increment(self):
        return 0.4

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):

    @property
    def weight_increment(self):
        return 0.3

    @property
    def allowed_food(self):
        return [Meat, Vegetable]

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    @property
    def weight_increment(self):
        return 1

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"
