from entity.product import Product

class Electronics(Product):
    def __init__(self, product_id, product_name, description, price, quantity_in_stock, type, brand, warranty_period):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, type)
        self.brand = brand
        self.warranty_period = warranty_period
