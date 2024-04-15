----------------------------------------
            Shop Management System
----------------------------------------

This Python program implements a simple shop management system where you can add products to a shop's inventory and buy products from the shop. It consists of two classes:

1. Product:
    - Represents a product with attributes such as ID, name, quantity, and unit price.

2. Shop:
    - Manages the shop's inventory and provides methods to add products and buy products.
    - The inventory of the shop is stored in a list called 'storage'.

----------------------------------------
             Functionality
----------------------------------------

1. Adding Products:
    - Use the add_product method of the Shop class to add products to the shop's inventory.
    - Each product requires an ID, name, quantity, and unit price.

2. Buying Products:
    - Use the buy_product method of the Shop class to buy products from the shop.
    - Specify the ID of the product you want to buy, the quantity you want to purchase, and the payment amount.
    - If the product is available in sufficient quantity and the payment is enough, the purchase is successful, and the change is calculated and returned.
    - If the product is not available or there is insufficient quantity, appropriate messages are displayed.

----------------------------------------
             Usage Example
----------------------------------------

# Create a shop instance
my_shop = Shop("Walmart")

# Add products to the shop
my_shop.add_product(1, 'Milk', 4, 5)
my_shop.add_product(2, 'Egg', 18, 2)
my_shop.add_product(3, 'Bread', 2, 3)
my_shop.add_product(4, 'Water', 20, 1)

# Display the shop's inventory
print(my_shop)

# Buy products from the shop
result = my_shop.buy_product(2, 4, 3)
print(result)

# Display the shop's updated inventory
print(my_shop)

