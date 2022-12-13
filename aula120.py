# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'andre'
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('André', 'Salvador')
# p1.nome = 'André'
# p1.sobrenome = 'Salvador'

p2 = Pessoa('Maria', 'Alves')
# p2.nome = 'Maria'
# p2.sobrenome = 'Alves'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)