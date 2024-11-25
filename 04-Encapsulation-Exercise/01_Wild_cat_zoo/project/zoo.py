from project.animal import Animal


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

    @staticmethod
    def __print_status(obj_list, *class_names):
        elements={name: [] for name in class_names}
        for obj in obj_list:
            elements[obj.__class__.__name__].append(repr(obj))
        result=[f"You have {len(obj_list)} {str(obj_list[0].__class__.__bases__[0].__name__).lower()}s"]
        for k, v in elements.items():
            result.append(f"----- {len(v)} {k}s:")
            result.extend(v)
        return "\n".join(result)

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    def animals_status(self):
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")
