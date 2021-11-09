# Exemplo 4

# definição de uma função que realiza a leitura
# de um inteiro e o retorna
def Le():# é uma função pois tem valor de retorno
  return int(input("Digite um inteiro: "))

def Adeus(): # é um procedimento pois não "retorna" nada para o ponto de chamado
  print("\nA execução deste programa terminou. Adiós.")

# início da função principal (função que realiza a chamada às outras funções)
r = Le()**Le()

print("{}".format(r))

Adeus()
