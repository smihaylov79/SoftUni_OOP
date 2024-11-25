from project.stores.base_store import BaseStore

class ToyStore(BaseStore):
    CAPACITY=100
    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        result = (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                  f"{self.get_estimated_profit()}\n**Toys for sale:")

        products_list = {}
        for product in self.products:
            if product.model not in products_list:
                products_list[product.model] = []
            products_list[product.model].append(product.price)
        sorted_products_list = sorted(products_list.items(), key=lambda x: x[0])
        for model in sorted_products_list:
            result += f"\n{model[0]}: {len(model[1])}pcs, average price: {sum(model[1]) / len(model[1]):.2f}"
        return result