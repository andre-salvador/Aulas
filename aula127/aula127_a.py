# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'C:\\Users\\André Salvador\\Desktop\\Aulas\\aula127\\'
CAMINHO_ARQUIVO +='aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def bom_dia(self):
        return f'Bom dia {self.nome}!! como você está?'

    def tchau(self):
        return f'Até mais {self.nome}, volte sempre!'


p1 = Pessoa('André', 22)
p2 = Pessoa('Maria', 20)
p3 = Pessoa('Silvia', 52)

bd = [vars(p1), p2.__dict__, vars(p3)]


if __name__ == '__main__':
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
        json.dump(bd, file, indent=2, ensure_ascii=False)