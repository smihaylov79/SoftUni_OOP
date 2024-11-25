from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):


    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0.0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def comp_type(self):
        pass

    @property
    def valid_ram(self):
        return [2**i for i in range(1, int(log2(self.max_ram))+1)]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.comp_type} {self.manufacturer} {self.model}!")
        if ram not in self.valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.comp_type} {self.manufacturer} {self.model}!")
        processor_price= self.available_processors[processor]
        ram_price= int(log2(ram)*100)
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price

        return f"Created {self.__repr__()} for {self.price}$."


    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
