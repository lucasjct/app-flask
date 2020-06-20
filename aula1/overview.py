#import OS
#itarage com o sistema operacional

#Posso utilizar o Ipthon no vsCode, chamando-o no terminal.
#Procurar o diretorio de um programa 'which python'


#Isolar Ambiente para no usar o sitema operacional

#python -m venv .venv
#Ativar ambiente


#arquivos

#f = open('readme.me').open

#open('readme.me', 'w').write("Hello") <- sobrescreve o conteúdo

#open('readme.me', 'e').write("help") < - não sobrescreve


#Tipos básicos de dados


#numero: int = 5
#fracao: float = 6.2
#online: bool = True
#texto:  str = '' <- strings é uma cadeia de bytes

#Python faz inferência de tipos para verifiar o tipo de variável, por isso posso declarar variáveis sem informar o tipo de dado.

#ex:

numero = 5
fracao = 6.2
online = True

#Python tem a opção id() para verificar a referência no endereço da memória. ex:

a = 12
b = 12

id(a)
id(b)

a is b # resultado é False
a == b # resultado é True porque verifica a os valores

# operação ternária
print("Ola" if a != b else "tchau")


##Tratamento de errros

num1 = 10
num = 0

## EAFP
try:
    num.upper()
    print(num1/num)
except AttributeError as e:
    print('Não posso fazer esse tipo de operação', str(e))
except ZeroDivisionError as e:
    print("Deu erro", str(e))


conter = "continue"

while conter == "continue":

    input("Deseja de continuar: ")
    break

#tipos compostos em python

cores = ["Verde", "Azul", "vermelho"]
numero = [1,2,3,4]
mistura = [1, "Bruno", 4.3, cores, numero, [1,2,3,4]]

cores.append("amArelo")
cores.inser(1, "branco")
print(cores)

#tuplas

identidade = ('Lucas', '33434454-5',15)

print(f'nome é: {identidade[1]}')

nome, cpf, idade = identidade

print(nome, cpf, idade)

#dicionario

pessoa = {  
    'nome': "lucas", 
    'cpf': "389U894=3", 
    'idade': 27,
    'cores': cores
    }

pessoa['idade'] = 34

for cor in cores:
    print(cor.upper())



for letra in 'Lucas':
    if letra == "u":
        continue
    print(letra)


print('Lucas[-1]')


#List Comprehension

print([letra for letra in 'Lucas'])

#List Comprehension Filtrada

print([letra for letra in 'Lucas' if letra != 'c'])

for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa.items():
    print(valor)