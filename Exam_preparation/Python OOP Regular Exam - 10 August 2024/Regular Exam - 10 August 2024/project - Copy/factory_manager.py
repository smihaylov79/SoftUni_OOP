from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        valid_types={'Chair':Chair, 'HobbyHorse':HobbyHorse}
        if product_type not in valid_types:
            raise Exception("Invalid product type!")
        product=valid_types[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        valid_types={'FurnitureStore':FurnitureStore, 'ToyStore':ToyStore}
        if store_type not in valid_types:
            raise Exception(f"{store_type} is an invalid type of store!")
        store=valid_types[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity<len(products):
            return f"Store {store.name} has no capacity for this purchase."
        sold=[]
        for product in products:
            if product.sub_type in store.store_type:
                sold.append(product)
        if sold:
            for product in sold:
                self.products.remove(product)
                store.products.append(product)
                store.capacity-=1
                self.income+=product.price
            return f"Store {store.name} successfully purchased {len(sold)} items."
        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        cur_store = next((s for s in self.stores if s.name==store_name), None)
        if cur_store is None:
            raise Exception("No such store!")
        if cur_store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(cur_store)
        return f"Successfully unregistered store {store_name}, location: {cur_store.location}."

    def discount_products(self, product_model: str):
        cur_prod=sum(1 for p in self.products if p.model==product_model)
        [p.discount() for p in self.products if p.model==product_model]
        return f"Discount applied to {cur_prod} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        cur_store=next((s for s in self.stores if s.name==store_name), None)
        if cur_store is None:
            return "There is no store registered under this name!"
        return cur_store.store_stats()

    def statistics(self):
        amount=sum(p.price for p in self.products)
        prod_models={}
        store_names=[s.name for s in self.stores]
        for product in self.products:
            if product.model not in prod_models:
                prod_models[product.model]=0
            prod_models[product.model]+=1
        result=f'Factory: {self.name}\nIncome: {self.income:.2f}\n***Products Statistics***'
        result+=f'\nUnsold Products: {len(self.products)}. Total net price: {amount:.2f}'
        for item in sorted(prod_models.items()):
            result+=f'\n{item[0]}: {item[1]}'
        result+=f'\n***Partner Stores: {len(store_names)}***\n'
        result+=f"{'\n'.join(sorted(store_names))}"
        return result

