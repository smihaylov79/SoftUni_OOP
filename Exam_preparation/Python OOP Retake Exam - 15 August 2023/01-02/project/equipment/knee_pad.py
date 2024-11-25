from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION=120
    PRICE=15
    PRICE_INCREASE=0.2
    EQ_TYPE='KneePad'
    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= (1+self.PRICE_INCREASE)
