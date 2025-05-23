from project.battleships.base_battleship import BaseBattleship


class BaseZone:
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: [BaseBattleship]=[]

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self._code = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume=value

    def get_ships(self):
        result=sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))
        return result


    def zone_info(self):
        pass