from abc import ABC, abstractmethod

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins=0
        self.equipment: [BaseEquipment]=[]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip()=='':
            raise ValueError("Team name cannot be empty!")
        self.__name=value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip())<2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country=value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value<=0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage=value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        result=f'Name: {self.name}\nCountry: {self.country}\nAdvantage: {self.advantage} points\nBudget: {self.budget:.2f}EUR\nWins: {self.wins}'
        eq_price=[e.price for e in self.equipment]
        eq_protection=[e.protection for e in self.equipment]
        result+=f'\nTotal Equipment Price: {sum(eq_price):.2f}\nAverage Protection: {int(sum(eq_protection)/len(eq_protection)) if eq_protection else 0}'
        return result
