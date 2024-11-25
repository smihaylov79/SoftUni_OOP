from project.animals.animal import Animal, Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def weight_increment(self):
        return 0.25
    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def weight_increment(self):
        return 0.35

    @property
    def allowed_food(self):
        return [Meat, Vegetable, Fruit, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"
