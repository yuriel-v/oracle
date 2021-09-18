class Produto:
    def __init__(self, price, name):
        self.price = price
        self.name = name
    
    def priceTag(self): 
        return f"{self.name};{self.price}"
        