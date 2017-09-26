
class Product:
    def __init__(self, name, price, count, tax):
        self.name = name
        self.price = price
        self.count = count
        self.tax = tax

    def price_with_tax(self):
        total = self.price * self.count * self.tax
        if total > 500:
           return 0.9 * total
        else:
           return total	



products = [Product(name="robot", price=900, count=2, tax=1.25), Product(name="bok", price=100, count=1, tax=1.06), Product(name="penna", price=50, count=2, tax=1.25)]

total_price = 0
for product in products:
    total_price = total_price + product.price_with_tax()
    print (product.price_with_tax())
print(total_price)





