# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - Iterável + Tamanho do grupo
# Permutação - Ordem Importa
# Produto - Ordem importa e repeta valores únicos
from itertools import combinations, permutations, product


def _print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['feminino', 'masculino', 'unisex'],
    ['algodão', 'poliéster'],
]


_print_iter(combinations(pessoas, 2))
_print_iter(permutations(pessoas, 2))
_print_iter(product(*camisetas))