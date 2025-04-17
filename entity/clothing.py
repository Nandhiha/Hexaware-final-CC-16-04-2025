from entity.product import Product

class Clothing(Product):
    def __init__(self, product_id, product_name, description, price, quantity_in_stock, type, size, color):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, type)
        self.size = size
        self.color = color
