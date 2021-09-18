from produtoUsado import ProdutoUsado
from produto import Produto
from produtoImportado import ProdutoImportado
n = input("Digite o número de produtos: ")

list1: list[Produto] = []

for i in range(int(n)):
    trigger = input("Digite o código do produto (c/u/i): ")
    price = input("Preço: ")
    name = input("Nome: ")
    if trigger == "c":
        commonProduct = Produto(float(price), name)
        list1.append(commonProduct)
    elif trigger == 'i':
        customFee = input("Taxa de alfândega: ")
        importedProduct = ProdutoImportado(float(price), name, float(customFee))
        list1.append(importedProduct)
    else:
        dataFabricacao = input("Data de fabricação: ")
        usedProduct = ProdutoUsado(float(price), name, dataFabricacao)
        list1.append(usedProduct)

print("\n")
for objects in list1:
    print(objects.priceTag() + "\n")
        