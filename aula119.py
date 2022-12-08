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


def mostrar_lista(lista):
    print()
    print('TAREFAS')
    for i in lista:
        print(i)
    print()


lista = []
desfazer = []

os.system('cls')
while True:
    print('Comandos: Listar, Desfazer, Refazer, Limpar tela')
    escolha = str(input('digite uma tafera ou comando: ')).lower()

    if escolha == 'listar':
        if len(lista) != 0:
            mostrar_lista(lista)
        else:
            print('Nada a mostrar')

    elif escolha == 'desfazer':
        if len(lista) != 0:
            desfazer.append(lista[-1])
            lista.pop()
            mostrar_lista(lista)
        
        else:
            print()
            print('Nada a desfazer')
            print()

    elif escolha == 'refazer':
        if len(desfazer) != 0:
            lista.append(desfazer[-1])
            desfazer.pop()
            mostrar_lista(lista)
        
        else:
            print()
            print('Não há mais itens para refazer')
            print()

    elif escolha == 'limpar tela':
        os.system('cls')
    
    else:
        if escolha not in lista:
            lista.append(escolha)
            mostrar_lista(lista)
        else:
            decisao = str(input('Você já adicionou essa terefa, deseja adicionar novamente? [S/N]? ')).lower()

            if decisao == 's':
                lista.append(escolha)
                mostrar_lista(lista)