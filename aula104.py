# Funções decoradoras e decoradores
# Docorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradores são funcções que docram outras Funções
# decoradores são usados para fazer o python usar as funções decoradoras em outras funções
# Decoradores são "Syntaz Sugar" (Açúcar sintático)


def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')



invertida = ('123')
print(invertida)