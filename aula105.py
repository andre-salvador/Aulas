#Decoradores com parâmetros
def parametros_decorador(nome):
    def decorador(func):
        print('Decoradora:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)