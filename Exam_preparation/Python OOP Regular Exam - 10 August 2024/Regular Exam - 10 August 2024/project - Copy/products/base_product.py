class BaseProduct:
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if len(value) < 3 or value.count(" ") == len(value):
            raise ValueError("Product model must be at least 3 chars long!")
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Product price must be greater than zero!")
        self._price = value

    def discount(self):
        pass