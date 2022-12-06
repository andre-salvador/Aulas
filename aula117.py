import json


caminho_arquivo = 'C:\\Users\\André Salvador\\Desktop\\Aulas\\aula117\\'
caminho_arquivo += 'aula117.json'

# pessoa = {
#     'nome': 'André Roberto',
#     'sobrenome': 'Salvador',
#     'endereco': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 7, 12),
#     'dev': True,
#     'nada': None,
# }

# with open(caminho_arquivo, 'w', encoding='utf-8') as file:
#     json.dump(
#         pessoa,
#         file,
#         ensure_ascii=False, # ensure_ascii é pra que ele coloque pontuação nas palavras
#         indent=2)

with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    pessoa = json.load(file)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])