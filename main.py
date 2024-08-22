print("Hello World!")

name = 'daniela'
type(name)

name = 12345
type(name)

for item in range (1,11):
    print(item)

vetor = [1, 2, 3, 4, 'daniela']
for item in vetor:
    print(item)

vetor = [1, 2, 3, 4, 5]
vetor = [1, 2, 3, 4, 'daneila']

for indice, valor in enumerate(vetor):
    print(indice,valor)

for indice, valor in enumerate(vetor):
    print(indice, valor)

vetor.reverse()


len(vetor)
5
vetor.reverse()

vetor.appende(3)

vetor.append(3)

vetor
[1, 2, 3, 4, 'daneila', 3]
vetor.reverse()
vetor
[3, 'daneila', 4, 3, 2, 1]
vetor.pop()
1
vetor
[3, 'daneila', 4, 3, 2]

sobrenome = 'serafim'
if nome and sobrenome:
    print(nome, sobrenome)

sobrenome = None
if nome and sobrenome:
    print(nome, sobrenome)


if nome and sobrenome:
    print(nome,sobrenome)
else:
    print('sobrenome nao informado')

    
'sobrenome nao informado'
if nome or sobrenome:
    print(nome, sobrenome)
else:
    print('sobrenome nao informado')


if sobrenome:
    print(sobrenome)
else:
    print('sobrenome nao informado')

    
'sobrenome nao informado'
sobrenome = 'Serafim'
if sobrenome:
    print(sobrenome)
else:
    print('sobrenome nao informado')

    
'Serafim'


valor = 10
lista = [1, 3, 4, 5, 7, 9, 10]
if valor > 10:
    print('maior')

    
if valor >= 10:
    print('maior ou igual')

    
'maior ou igual'
if valor <= 10:
    print('menor ou igual')

    
'menor ou igual'
if valor < 10:
    print('menor')

    
valor = 5
if valor < 10:
    print('menor')

    
'menor'
lista
[1, 3, 4, 5, 7, 9, 10]
valor
5
if valor in lista:
    print('está contido na lista')

    
'está contido na lista'
if 2 in lista:
    print('está contido na lista')

    
if 2 not in lista:
    print('nao está contidoc na lista')

class MinhaClasse:
    """Documentacao da classe"""

    atributo_publico = None
    __atributo_privado = 5

    def __init__(self) -> None:
        self.atributo_publico = 10

    def metodo(self):
        return self.atributo_publico * 2
    
    def get_atributo_privado(self):
        return self.__atributo_privado
instancia = MinhaClasse()
