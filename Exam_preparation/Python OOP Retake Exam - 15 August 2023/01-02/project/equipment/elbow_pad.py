from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION=90
    PRICE=25
    PRICE_INCREASE=0.1
    EQ_TYPE = 'ElbowPad'
    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= (1+self.PRICE_INCREASE)