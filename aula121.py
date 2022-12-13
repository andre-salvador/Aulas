# Métodos em instâncias de classes Python
# Had coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('celta')
print(celta.nome)
celta.acelerar()