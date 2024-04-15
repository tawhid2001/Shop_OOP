        
class Product:
    def __init__(self,product_id,product_name,quantity,unit_price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

class Shop:
    storage = []

    def __init__(self,shop_name):
        self.shop_name = shop_name

    def add_product(self,id,name,quantity,unit_price):
        product = Product(id,name,quantity,unit_price)
        self.storage.append(product)

    def buy_product(self, id, quantity, payment):
        for product in self.storage:
            if product.product_id == id:
                if product.quantity >= quantity:
                    price = quantity * product.unit_price
                    if price <= payment:
                        product.quantity -= quantity
                        change = payment - price
                        return f"Product ID: {product.product_id} Product Name: {product.product_name} has been successfully bought. Here is your change: {change}"
                    else:
                        return "Please pay more."
                else:
                    return "Insufficient quantity."
        return "Product is not available in the shop."
    
    def __repr__(self):
        products_info = "\n".join([f"ID: {product.product_id}, Name: {product.product_name}, Quantity: {product.quantity}, Unit Price: {product.unit_price}" for product in self.storage])
        return f"---------------{self.shop_name} -------------\n{products_info}"


            

my_shop = Shop("Walmart")
my_shop.add_product(1,'Milk',4,5)
my_shop.add_product(2,'egg',18,2)
my_shop.add_product(3,'Bread',2,3)
my_shop.add_product(4,'Water',20,1)

print(my_shop)

result = my_shop.buy_product(2,4,3)
print(result)

print(my_shop)