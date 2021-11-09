# Exemplo 3

# definição de uma função que realiza a leitura
# de um inteiro e o retorna
def Le():# é uma função pois tem valor de retorno
  return int(input("Digite um inteiro: "))

def Adeus(): # é um procedimento pois não "retorna" nada para o ponto de chamado
  print("\nA execução deste programa terminou. Adiós.")

# início da função principal (função que realiza a chamada às outras funções)
a = Le()
b = Le()
r = a**b

print("{} elevado a {} é {}".format(a, b, r))

Adeus()
