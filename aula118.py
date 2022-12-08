# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('andre',)
adiciona_clientes('joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Marcos')

cliente2= adiciona_clientes('maria')
adiciona_clientes('joão', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vitória', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
