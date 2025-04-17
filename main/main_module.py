import pyodbc 
import sys, os
# add the project root (one level up from main/) to the module search path
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from dao.order_processor import OrderProcessor
from entity.user import User
from entity.product import Product
from entity.electronics import Electronics
from entity.clothing import Clothing
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException
from exception.invalid_role_exception import InvalidRoleException

def main():
    processor = OrderProcessor()

    while True:
        print("\n===== ORDER MANAGEMENT SYSTEM =====")
        print("1. Create User")
        print("2. Create Product")
      
        print("3. Cancel Order")
        print("4. Get All Products")
        print("5. Get Orders by User")
        print("6. View Table")  
        print("7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                
                user_id = int(input("User ID: "))
                username = input("Username: ")
                password = input("Password: ")
                role = input("Role (Admin/User): ")
                user = User(user_id, username, password, role)
                processor.create_user(user)
                print("✅ User created successfully.")

            elif choice == "2":
                
                user_id = int(input("Enter Admin User ID: "))
                username = input("Enter Admin Username: ")
                password = input("Enter Admin Password: ")
                role = input("Enter Role (Admin): ")
                user = User(user_id, username, password, role)

                product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                description = input("Description: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity In Stock: "))
                ptype = input("Type (Electronics/Clothing): ")

                if ptype.lower() == "electronics":
                    brand = input("Brand: ")
                    warranty = int(input("Warranty Period (months): "))
                    product = Electronics(product_id, product_name, description, price, quantity, ptype, brand, warranty)
                elif ptype.lower() == "clothing":
                    size = input("Size: ")
                    color = input("Color: ")
                    product = Clothing(product_id, product_name, description, price, quantity, ptype, size, color)
                else:
                    print("❌ Invalid product type.")
                    continue

                processor.create_product(user, product)
                print("✅ Product created successfully.")

            elif choice == "8":
               
                user_id = int(input("User ID: "))
                username = input("Username: ")
                password = input("Password: ")
                role = input("Role (User): ")
                user = User(user_id, username, password, role)

                num = int(input("How many products to order? "))
                products = []
                for i in range(num):
                    pid = int(input(f"Enter Product ID {i+1}: "))
                   
                    products.append(Product(pid, "", "", 0, 0, ""))

                processor.create_order(user, products)
                print("✅ Order created successfully.")

            elif choice == "3":
             
                user_id = int(input("User ID: "))
                order_id = int(input("Order ID to cancel: "))
                processor.cancel_order(user_id, order_id)
                print("✅ Order canceled successfully.")

            elif choice == "4":
               
                products = processor.get_all_products()
                print("\n📦 All Products:")
                for p in products:
                    print(p)

            elif choice == "5":
    
                user_id = int(input("User ID: "))
                username = input("Username: ")
                password = input("Password: ")
                role = input("Role: ")
                user = User(user_id, username, password, role)
                orders = processor.get_order_by_user(user)
                print("\n🧾 Orders by User:")
                for o in orders:
                    print(o)

            elif choice == "6":
                
                table_name = input("Enter the table name to view (users, products, orders, etc.): ")
                view_table(table_name)

            elif choice == "7":
               
                print("👋 Exiting... Thank you!")
                break

            else:
                print("❌ Invalid choice. Try again.")

        except UserNotFoundException as e:
            print(f"❗ Error: {e}")
        except OrderNotFoundException as e:
            print(f"❗ Error: {e}")
        except InvalidRoleException as e:
            print(f"❗ Error: {e}")
        except Exception as e:
            print(f"❗ Unexpected Error: {e}")

def view_table(table_name):

    conn = get_connection()
    cursor = conn.cursor()

  
    query = f"SELECT * FROM {table_name}"

    try:
       
        cursor.execute(query)

        
        rows = cursor.fetchall()

       
        if rows:
            for row in rows:
                print(row)
        else:
            print(f"No data found in {table_name}.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        
        cursor.close()
        conn.close()

def get_connection():
   
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-6PSEMB9\\NANDHIHA;"  
        "Database=ordermanagementsystem;" 
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

if __name__ == "__main__":
    main()
