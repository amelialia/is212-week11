class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name}: {discounted_price}")
        return discounted_price

    def calculate_tax(self, tax_rate):
        tax = self.price * tax_rate
        print(f"Tax for {self.name}: {tax}")
        return tax

class Electronics(Product):
    def apply_discount(self):
        return super().apply_discount(0.10)  # 10% discount

    def calculate_tax(self):
        return super().calculate_tax(0.15)  # 15% tax

class Clothing(Product):
    def apply_discount(self):
        return super().apply_discount(0.20)  # 20% discount

    def calculate_tax(self):
        return super().calculate_tax(0.08)  # 8% tax

class Grocery(Product):
    def apply_discount(self):
        return super().apply_discount(0.05)  # 5% discount

    def calculate_tax(self):
        return super().calculate_tax(0.02)  # 2% tax

