class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type=topping_type
        self.weight=weight
        
    @property
    def topping_type(self):
        return self.__topping_type
    
    @topping_type.setter
    def topping_type(self, value):
        if value=="":
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type=value
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value<=0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight=value
        
class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.baking_technique=baking_technique
        self.flour_type=flour_type
        self.weight=weight
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value<=0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight=value
    
    @property
    def flour_type(self):
        return self.__flour_type
    
    @flour_type.setter
    def flour_type(self, value):
        if value=="":
            raise ValueError("The topping type cannot be an empty string")
        self.__flour_type=value
    
    @property
    def baking_technique(self):
        return self.__baking_technique
    
    @baking_technique.setter
    def baking_technique(self, value):
        if value=="":
            raise ValueError("The topping type cannot be an empty string")
        self.__baking_technique=value

class Pizza:
    def __init__(self, name, dough, max_number_of_toppings):
        self.name=name
        self.dough=dough
        self.max_number_of_toppings=max_number_of_toppings
        self.toppings={}
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value=="":
            raise ValueError("The name type cannot be an empty string")
        self.__name=value
        
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough=value
        
    
    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings
    
    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value<=0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings=value
    
    def add_topping(self, topping):
        if len(self.toppings)==self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type]=0
        self.toppings[topping.topping_type]+=topping.weight
    
    def calculate_total_weight(self):
        return self.dough.weight+sum(self.toppings.values())


tomato_topping = Topping("Tomato", 60)
print(tomato_topping.topping_type)
print(tomato_topping.weight)
mushrooms_topping = Topping("Mushroom", 75) 
print(mushrooms_topping.topping_type) 
print(mushrooms_topping.weight)
mozzarella_topping = Topping("Mozzarella", 80)
print(mozzarella_topping.topping_type)
print(mozzarella_topping.weight)
cheddar_topping = Topping("Cheddar", 150)
pepperoni_topping = Topping("Pepperoni", 120)
white_flour_dough = Dough("White Flour", "Mixing", 200)
print(white_flour_dough.flour_type)
print(white_flour_dough.weight)
print(white_flour_dough.baking_technique)
whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
print(whole_wheat_dough.weight)
print(whole_wheat_dough.flour_type)
print(whole_wheat_dough.baking_technique)
p = Pizza("Margherita", whole_wheat_dough, 2)
p.add_topping(tomato_topping)
print(p.calculate_total_weight())
p.add_topping(mozzarella_topping)
print(p.calculate_total_weight())
p.add_topping(mozzarella_topping) 