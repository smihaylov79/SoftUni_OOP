from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OX_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, self.OX_LEVEL)

    def renew_oxy(self):
        self.oxygen_level = self.OX_LEVEL

    def miss(self, time_to_catch: int):
        value_to_reduce = round(time_to_catch * 0.3)
        if self.oxygen_level < value_to_reduce:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= value_to_reduce