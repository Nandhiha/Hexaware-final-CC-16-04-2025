import pyodbc
from dao.iorder_management_repository import IOrderManagementRepository
from entity.user import User
from entity.product import Product
from entity.electronics import Electronics
from entity.clothing import Clothing
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException
from exception.invalid_role_exception import InvalidRoleException
from util.db_conn_util import get_connection

class OrderProcessor(IOrderManagementRepository):

    def create_user(self, user: User):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (userid, username, password, role) VALUES (?, ?, ?, ?)",
                           user.user_id, user.username, user.password, user.role)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def create_product(self, user: User, product: Product):
        if user.role.lower() != "admin":
            raise InvalidRoleException("Only admin can create products.")

        conn = get_connection()
        cursor = conn.cursor()
        try:
          
            cursor.execute(
                "INSERT INTO products (productid, productname, description, price, quantityinstock, type) VALUES (?, ?, ?, ?, ?, ?)",
                product.product_id, product.product_name, product.description,
                product.price, product.quantity_in_stock, product.type
            )

         
            if product.type.lower() == "electronics" and isinstance(product, Electronics):
                cursor.execute(
                    "INSERT INTO electronics (productid, brand, warrantyperiod) VALUES (?, ?, ?)",
                    product.product_id, product.brand, product.warranty_period
                )
            elif product.type.lower() == "clothing" and isinstance(product, Clothing):
                cursor.execute(
                    "INSERT INTO clothing (productid, size, color) VALUES (?, ?, ?)",
                    product.product_id, product.size, product.color
                )

            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def create_order(self, user: User, products: list):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            
            cursor.execute("SELECT * FROM users WHERE userid = ?", user.user_id)
            if cursor.fetchone() is None:
                self.create_user(user)

            cursor.execute("SELECT MAX(orderid) FROM orders")
            max_orderid = cursor.fetchone()[0]
            if max_orderid is None:  
                order_id = 1
            else:
                order_id = max_orderid + 1 

           
            cursor.execute("INSERT INTO orders (orderid, userid) VALUES (?, ?)",
                           order_id, user.user_id)
            
         
            for idx, product in enumerate(products, start=1):
                cursor.execute(
                    "INSERT INTO order_details (orderid, productid, quantity) VALUES (?, ?, ?)",
                    order_id, product.product_id, 1  
                )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def cancel_order(self, user_id: int, order_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE userid = ?", user_id)
            if cursor.fetchone() is None:
                raise UserNotFoundException("User ID not found.")

            cursor.execute("SELECT * FROM orders WHERE orderid = ?", order_id)
            if cursor.fetchone() is None:
                raise OrderNotFoundException("Order ID not found.")

            cursor.execute("DELETE FROM order_details WHERE orderid = ?", order_id)
            cursor.execute("DELETE FROM orders WHERE orderid = ?", order_id)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def get_all_products(self) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
            products = []
            for row in rows:
                products.append({
                    'ProductID': row.productid,
                    'ProductName': row.productname,
                    'Description': row.description,
                    'Price': row.price,
                    'Stock': row.quantityinstock,
                    'Type': row.type
                })
            return products
        finally:
            cursor.close()
            conn.close()

    def get_order_by_user(self, user: User) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(""" 
                SELECT od.orderid, p.productname, od.quantity
                FROM order_details od
                JOIN orders o ON od.orderid = o.orderid
                JOIN products p ON od.productid = p.productid
                WHERE o.userid = ? 
            """, user.user_id)
            orders = cursor.fetchall()
            order_list = []
            for order in orders:
                order_list.append({
                    'OrderID': order.orderid,
                    'ProductName': order.productname,
                    'Quantity': order.quantity
                })
            return order_list
        finally:
            cursor.close()
            conn.close()
