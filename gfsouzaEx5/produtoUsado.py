from produto import Produto

class ProdutoUsado(Produto):
    def __init__(self, price, name, manufactDate):
        super().__init__(price, name)
        self.manufactDate = manufactDate
        
    def priceTag(self):
        return f"{super().priceTag()};{self.manufactDate}"