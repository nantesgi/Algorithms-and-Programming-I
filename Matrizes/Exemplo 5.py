# Exemplo 5

# criando uma lista vazia (que será uma matriz!)
matriz = []

while True:
  print("Digite a dimensão da matriz: ")
  m = int(input())
  if (m > 0):
    break;

# tem m positivo 

# lendo a matriz linha por linha
for i in range(m):
  # variável auxiliar para 
  linha = []
  linha = list(map(int, input().split()))

  matriz.append(linha)

for i in range(m):
  # para imprimir a diagonal principal
  print(" "*i, matriz[i][i])