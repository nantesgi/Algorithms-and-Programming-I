# Exemplo 3

# inicializando um matriz de dimensão n X m com o valor zero

n = int(input('Digite a dimensão n (linhas) da matriz: '))
m = int(input('Digite a dimensão m (colunas) da matriz: '))

#lista de dados!
matriz = []

# cria e inicializa da uma das n linhas da matriz
for i in range(n):
    matriz.append([0]*m) # [0]*m --> este comando gera uma lista onde todos os seus m elementos possuem valor igual a zero
    #matriz.append([9]*m) # [0]*m --> este comando gera uma lista onde todos os seus m elementos possuem valor igual a nove
    #matriz.append(['*']*m) # [0]*m --> este comando gera uma lista onde todos os seus m elementos possuem valor igual a zero

print(matriz)

# linha i da matriz
for i in range(0, n):
  # colunas j da linha i
  for j in range(m): # impressão das colunas da linha i
    print(matriz[i][j], end=' ')
  print()
