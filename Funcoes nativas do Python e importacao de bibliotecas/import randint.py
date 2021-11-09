# import randint

#importando o módulo randint do pacote random e fazendo o acesso aos mesmo
# pelo identificador "r" e não "randint"
from random import randint as r
num = r(0, 10)
print(f'O número aleatório de 0 a 10 gerado foi: {num}.')

#https://docs.python.org/3/library/random.html