# Exemplo 5

# definição de uma função que realiza a leitura
# de um inteiro e o retorna
def Le():
  return int(input("Digite um inteiro: "))

# definição da função de calcula o valor de x**y
# esta função possui dois parâmetros de entrada (parâmetros formais da função)
def Potencia(x, y):
  return x**y


# início da função principal - main()
a = Le()
b = Le() # sem argumentos de entrada
r = Potencia(a,b) # a e b são os argumentos de entrada da função Potência

print("{} elevado a {} é {}".format(a, b, r))

# r = Potencia(b,a) #a e b são os argumentos de entrada da função Potência