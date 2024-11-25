class BaseBattleship:
    def __init__(self, name, health, hit_strength, ammunition):
        self.name=name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking = False
        self.is_available = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self._name=value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value<0:
            self.health=0
        self._health=value

    def take_damage(self, enemy_battleship):
        self.health-=enemy_battleship.hit_strength

    def attack(self):
        pass
