import json
import os


# pessoas = [
#     {
#         "nome": "Maria",
#         "sobrenome": "Vieira",
#         "idade": 25,
#         "ativo": False,
#         'notas': ['A', 'A+'],
#         "telefones": {
#             "residencial": "00 0000-0000",
#             "celular": "00 00000-0000",
#         },
#     },
#     {
#         "nome": "Marcos",
#         "sobrenome": "Santana",
#         "idade": 23,
#         "ativo": True,
#         'notas': ['B', 'A'],
#         "telefones": {
#             "residencial": "00 0000-0000",
#             "celular": "00 00000-0000",
#         }
#     },
#     {
#         "nome": "Joana",
#         "sobrenome": "Moreira",
#         "idade": 32,
#         "ativo": False,
#         'notas': ['A', 'A+'],
#         "telefones": {
#             "residencial": "00 0000-0000",
#             "celular": "00 00000-0000",
#         }
#     }
# ]

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(SAFE_TO, 'w') as file:
#     json.dump(pessoas, file, indent=2)

# print(json.dumps(pessoas, indent=2))

# with open(JSON_FILE, 'r') as file:
#     pessoas = json.load(file)
#     print(json.dumps(pessoas))

    # for pessoa in pessoas:
    #     print(pessoa['nome'])

json_string = '''
[{"nome": "Maria", "sobrenome": "Vieira", "idade": 25, "ativo": false, "notas": ["A", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 00000-0000"}}, {"nome": "Marcos", "sobrenome": "Santana", "idade": 23, "ativo": true, "notas": ["B", "A"], "telefones": {"residencial": "00 0000-0000", "celular": "00 00000-0000"}}, {"nome": "Joana", "sobrenome": "Moreira", "idade": 32, "ativo": false, "notas": ["A", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 00000-0000"}}]
'''

pessoas = json.loads(json_string)

for pessoa in pessoas:
    print(pessoa['nome'])