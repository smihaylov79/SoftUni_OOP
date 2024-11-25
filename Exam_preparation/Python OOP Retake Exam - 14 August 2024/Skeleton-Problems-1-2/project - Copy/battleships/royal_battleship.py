from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    AMMUNITION=100
    USED_AMMO=25
    def __init__(self, name, health, hit_strenght):
        super().__init__(name, health, hit_strenght, self.AMMUNITION)
        self.ship_type='RoyalBattleship'

    def attack(self):
        self.ammunition-=self.USED_AMMO
        if self.ammunition <= 0:
            self.ammunition=0