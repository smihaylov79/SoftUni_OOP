from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    AMMUNITION=80
    USED_AMMO=10
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMUNITION)
        self.ship_type='PirateBattleship'

    def attack(self):
        self.ammunition-=self.USED_AMMO
        if self.ammunition <= 0:
            self.ammunition = 0
