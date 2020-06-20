def ola(nome):
    print('ola: ', nome)

ola('Lucas')
ola('Maina')
ola('Diego')

#Argumentos, parâmetros, encapsulamento
#Funções são preguiçosas porque precisam ser chamadas para serem executadas
# def = define functions

#Parâmetros posicionais e nomeados


def ola(nome, maiusculo=False):
    if maiusculo:
        msg = 'ola: ', nome.upper()
    else:
        msg = 'ola: ', nome

    print(msg)

ola("Lucas", True)

#Funções dentro de funções Utilidade
#Funções não devem receber muitos argumentos (mais de 8 fica complexa a manutenção)
def ola(nome, maiusculo=False):
    if maiusculo:
        msg = 'ola: ', nome.upper()
    else:
        msg = 'ola: ', nome

    print(msg)

ola("Lucas", True)

#desenpacotamento, *
def hello (nome, cpf, idade=0):
    print('olá', nome, cpf, idade)

#pessoa = ["Lucas", '667676-99', 15]

#hello(*pessoa)

#com dicionários (dois asteriscos)
pessoa = {
    'nome': 'Lucas',
    'cpf': '12345-55',
    'idade': 15
}

hello(**pessoa)


#Utilizando argumentos não definidos, get all
#útil para funções genéricas, utilizadas para frameworks, etc
def helloWord (nome, cpf, idade=0, *args, **kwargs):

    print('olá', nome.upper(), cpf, idade)
    print(args)
    print(kwargs)

helloWord('lucas', '48484848-44', 16, cor = 'pardo', foo = 'bar', outra_coisa = 1)


#Função void, seu resultado vai para o vacuo
def ola():
    print('Olá')

ola()

#função com retorno
#no Python 3^ podemos especificar o tipo da variável que será parâmetro na função

def soma(a: int, b: int)->int:
    resultado = a + b
    return resultado

result = soma(1,69)
result


#funções são cidadãos de primeira classe

def mensagem(header, footer):
    
    header = header()
    print('Olá você está no CodeShow')
    footer = footer()

def header():
    print('****Inicio****')

def footer():
    print('****Fim****')


##Decorator é uma função que recebe outra função
def header(f): # 'f' de function
    def decorator(nome):
        print("###Bem Vindo ao meu site ###")
        print("")
        return f(nome)
    return decorator

def footer(f):
    def decorator(nome):
        print('Copyright 2020')
        return f(nome)
    return decorator

@footer
@header
def produto(nome):
    print('Produto:', nome, 'R$ 2K')


produto('Cadeira')

#com decorator

def pao(f):
    def wrapper(recheio):
        print("(fatia superior pão)")
        f()
        print("(fatia inferior do pão)")
    return wrapper


@pao
def lanche():
    print('Hamburguer vegano')

@pao
def opa():
    print('...')
opa()