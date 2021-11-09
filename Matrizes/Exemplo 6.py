# Exemplo 6

# criando uma lista vazia (que será uma matriz!)
matriz = []

while True:
  print("Digite a dimensão da sua matriz quadrada: ")
  m = int(input())
  if (m > 0):
    break;

# tem m positivo 

# lendo a matriz linha por linha
for i in range(m):
  # variável auxiliar para 
  linha = []
  print("Digite os elementos da linha {}: ".format(i+1))
  linha = list(map(int, input().split()))

  matriz.append(linha)

for i in range(m):
  # para imprimir a diagonal secundária
  print(" "*(m-i-1), matriz[i][m-i-1])
  # print(matriz[i][m-i-1])