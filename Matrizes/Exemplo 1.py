# Exemplo 1

# todas as linhas da matriz possui a mesma quantidade de elementos
matriz = [[4, 23, 12, 4] , [5, 6, 7, 13] , [32, 37, 2, -1]]

# primeiro elemento da matriz: [4, 23, 12, 4]
# segundo elemento da matriz:  [5, 6, 7, 13]
# terceiro elemento da matriz: [32, 37, 2, -1]

# imprimindo toda a lista/matriz
print(matriz)


# imprimindo cada uma das linhas da lista/matriz
print(matriz[0])  # primeiro elemento da matriz: [4, 23, 12, 4]
print(matriz[1])  # segundo elemento da matriz:  [5, 6, 7, 13]
print(matriz[2]) # terceiro elemento da matriz: [32, 37, 2, -1]
print()

for i in range(0, 3):#i = 0, 1, 2
  # j =  0, 1, 2, 3
  for j in range(4): # impressão das colunas da linha i
    print("{:6.0f}". format(matriz[i][j]), end=' ')
  print()

print()
linhas = len(matriz) # quanto elementos tem na matriz? 3 (3 listas!)
print("A matriz tem {} linhas".format(linhas))

colunas = len(matriz[0])
print("A matriz tem {} colunas.".format(colunas))