from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OX_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.OX_LEVEL)

    def renew_oxy(self):
        self.oxygen_level=self.OX_LEVEL

    def miss(self, time_to_catch: int):
        value_to_reduce=round(time_to_catch*0.6)
        if self.oxygen_level<value_to_reduce:
            self.oxygen_level=0
        else:
            self.oxygen_level=self.oxygen_level- value_to_reduce
