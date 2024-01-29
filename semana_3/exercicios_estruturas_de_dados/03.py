""" Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra. """

compra_supermercado = {
    'Maçãs': 5,
    'Bananas': 3,
    'Leite': 2,
    'Pão': 1,
    'Ovos': 12,
    'Arroz': 1,
    'Feijão': 2,
    'Cenouras': 4,
    'Tomates': 6,
    'Sabonete': 2
}

quantidade = sum(compra_supermercado.values())
print(quantidade)