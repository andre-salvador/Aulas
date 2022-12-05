# reduce - faz a redução de um iterável em um valor
from functools import reduce

# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0
)

print('total é', total)

# acumulador = 0
# for p in produtos:
#     acumulador += p['preco']

# print(acumulador)

# print(sum([p['preco'] for p in produtos]))