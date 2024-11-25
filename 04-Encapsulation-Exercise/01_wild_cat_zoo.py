class Animal:
    def __init__(self, name, gender, age, money_for_care):
        self.name=name
        self.gender=gender
        self.age=age
        self.money_for_care=money_for_care
        
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
        

# Lion
class Lion(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 50)
        
        
class Tiger(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)
        
class Cheetah(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 60)
        
class Worker:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
        

class Keeper(Worker):
    pass

class Caretaker(Worker):
    pass

class Vet(Worker):
    pass


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name=name
        self.__budget=budget
        self.__animal_capacity=animal_capacity
        self.__workers_capacity=workers_capacity
        self.animals=[]
        self.workers=[]
        
    def add_animal(self, animal:Animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget<price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        
    def hire_worker(self, worker):
        if self.__workers_capacity<=len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        
    def fire_worker(self, worker_name):
        worker=next((w for w in self.workers if w.name==worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"
        
    def pay_workers(self):
        total_salaries=sum(w.salary for w in self.workers)
        if self.__budget<total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        
    def tend_animals(self):
        total_money_for_care=sum(a.money_for_care for a in self.animals)
        if self.__budget<total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget-=total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        
    def profit(self, amount):
        self.__budget +=amount
        
    def animals_status(self):
        lions=[]
        tigers=[]
        cheetahs=[]
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(repr(animal))
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(repr(animal))
        result=[f"You have {len(self.animals)} animals"]
        result.append(f"----- {len(lions)} Lions:")
        result.extend(lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)
        
        return "\n".join(result)
        
    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")
    
    @staticmethod
    def __print_status(obj_list, *class_names):
        elements={name: [] for name in class_names}
        for obj in obj_list:
            elements[obj.__class__.__name__].append(repr(obj))
        result=[f"You have {len(obj_list)} {str(obj_list[0].__class__.__bases__[0].__name__).lower()}s"]
        for k, v in elements.items():
            result.append(f"----- {len(v)} {k}s")
            result.extend(v)
        return "\n".join(result)


zoo = Zoo("Zootopia", 3000, 5, 8) 

 

# Animals creation 

animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)] 

 

# Animal prices 

prices = [200, 190, 204, 156, 211, 140] 

 

# Workers creation 

workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)] 

 

# Adding all animals 

for i in range(len(animals)): 

    animal = animals[i] 

    price = prices[i] 

    print(zoo.add_animal(animal, price)) 

 

# Adding all workers 

for worker in workers: 

    print(zoo.hire_worker(worker)) 

 

# Tending animals 

print(zoo.tend_animals()) 

 

# Paying keepers 

print(zoo.pay_workers()) 

 

# Fireing worker 

print(zoo.fire_worker("Adam")) 

 

# Printing statuses 

print(zoo.animals_status()) 

print(zoo.workers_status()) 