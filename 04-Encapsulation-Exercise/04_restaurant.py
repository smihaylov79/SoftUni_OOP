class Product:
    def __init__(self, name, price):
        self.__name=name
        self.__price=price
    
    @property
    def name(self):
        return self.__name
        
    @property
    def price(self):
        return self.__price

class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams=grams
    
    @property
    def grams(self):
        return self.__grams

class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters=milliliters
    
    @property
    def milliliters(self):
        return self.__milliliters

class MainDish(Food):
    pass

class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories=calories
    
    @property
    def calories(self):
        return self.__calories

class Starter(Food):
    pass

class Salmon(MainDish):
    GRAMS = 22
    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)

    
class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5
    def __init__(self, name):
        super().__init__(name, self.Price, self.Grams, self.CALORIES)
    

class Soup(Starter):
    pass

class HotBeverage(Beverage):
    pass

class ColdBeverage(Beverage):
    pass

class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    def __init__(self, name, caffeine):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine=caffeine
    
    @property
    def caffeine(self):
        return self.__caffeine

class Tea(HotBeverage):
    pass


product = Product("coffee", 2.5) 

print(product.__class__.__name__) 

print(product.name) 

print(product.price) 

beverage = Beverage("coffee", 2.5, 50) 

print(beverage.__class__.__name__) 

print(beverage.__class__.__bases__[0].__name__) 

print(beverage.name) 

print(beverage.price) 

print(beverage.milliliters) 

soup = Soup("fish soup", 9.90, 230) 

print(soup.__class__.__name__) 

print(soup.__class__.__bases__[0].__name__) 

print(soup.name) 

print(soup.price) 

print(soup.grams) 
    