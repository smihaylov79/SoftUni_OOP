class Vet:
    animals: list[str] = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals: list[str] = []

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            # Vet.space-=1
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            # Vet.space+=1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"
