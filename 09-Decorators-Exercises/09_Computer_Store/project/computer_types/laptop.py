from project.computer_types.computer import Computer


class Laptop(Computer):
    RAM_MAX = 64

    @property
    def available_processors(self):
        return {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}

    @property
    def max_ram(self):
        return self.RAM_MAX

    @property
    def comp_type(self):
        return "laptop"

