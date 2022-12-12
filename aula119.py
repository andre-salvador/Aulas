# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json


CAMINHO = 'C:\\Users\\André Salvador\\Desktop\\Aulas\\aula119\\'
CAMINHO += 'aula119.json'
def mostrar_lista(lista):
    if not lista:
        print()
        print('Nada a ser mostrado')
        print()
        return

    print()
    print('TAREFAS')
    for i in lista:
        print(i)
    print()

def desfazer_lista(lista, desfazer):
    if not lista:
        print('Nada a desfazer')
        return
    
    desfazer.append(lista[-1])
    lista.pop()
    mostrar_lista(lista)

def refazer_lista(lista, desfazer):
    if not desfazer:
        print('Não há mais itens para refazer')
        return

    lista.append(desfazer[-1])
    desfazer.pop()
    mostrar_lista(lista)

def adicionar(escolha, lista):
    if escolha not in lista:
        lista.append(escolha)
        mostrar_lista(lista)
    else:
        decisao = str(input('Você já adicionou essa terefa, deseja adicionar novamente? [S/N]? ')).lower()

        if decisao == 's':
            lista.append(escolha)
            mostrar_lista(lista)

def criar_json(lista, CAMINHO):
    dados = lista
    with open(CAMINHO, 'w', encoding='utf-8') as file:
        dados = json.dump(lista, file, ensure_ascii=False, indent=2,)
    return dados

def ler(lista, CAMINHO):
    dados = []
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as file:
            dados = json.load(file)
            mostrar_lista(lista)
    
    except FileNotFoundError:
        print('O arquivo não existe')
        criar_json(lista, CAMINHO)

    return dados

lista = ler([], CAMINHO)
desfazer = []

os.system('cls')
while True:
    print('Comandos: Listar, Desfazer, Refazer, clear')
    escolha = str(input('digite uma tafera ou comando: ')).lower()

    comandos = {
            'listar': lambda: mostrar_lista(lista),
            'desfazer': lambda: desfazer_lista(lista, desfazer),
            'refazer': lambda: refazer_lista(lista, desfazer),
            'clear': lambda: os.system('cls'),
            'adicionar': lambda: adicionar(escolha, lista)
        }

    comando = comandos.get(escolha) if comandos.get(escolha) is not None else comandos['adicionar']
    comando()
    
    criar_json(lista, CAMINHO)

#     if escolha == 'listar':
#         mostrar_lista(lista)

#     elif escolha == 'desfazer':
#         desfazer_lista(lista, desfazer)

#     elif escolha == 'limpar tela':
#         os.system('cls')
    
#     else:
#         if escolha not in lista:
#             lista.append(escolha)
#             mostrar_lista(lista)
#         else:
#             decisao = str(input('Você já adicionou essa terefa, deseja adicionar novamente? [S/N]? ')).lower()

#             if decisao == 's':
#                 lista.append(escolha)
#                 mostrar_lista(lista)
