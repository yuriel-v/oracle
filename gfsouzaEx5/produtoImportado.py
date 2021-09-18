from produto import Produto;

class ProdutoImportado(Produto):
    def __init__(self, price, name, customFee):
        super().__init__(price, name)
        self.customFee = customFee
    
    def priceTag(self):
        return f"{self.name};{self.totalPrice()};{self.customFee}"

    def totalPrice(self):
        return self.price + self.customFee
