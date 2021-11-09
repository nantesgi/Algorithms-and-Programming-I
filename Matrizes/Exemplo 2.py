# Exemplo 2

# cada linha da matriz pode possuir uma quantidade específica de elementos
matriz = [[4], [5, 6, 7, 3, 6, -12, 13], [32, 2, -1]]

# primeiro elemento da matriz: [4]
# segundo elemento da matriz:  [5, 6, 7, 3, 6, -12, 13]
# terceiro elemento da matriz: [32, 2, -1]

# imprimindo toda a lista/matriz
print(matriz)


# imprimindo cada uma das linhas da lista/matriz
print(matriz[0])
print(matriz[1])
print(matriz[2])
print()

#i percorre as linhas
for i in range(0, 3):
  # j percorre as colunas da linha i
  # len(matriz[i]) retorna a quantidade de elementos da linha i
  for j in range(len(matriz[i])): # impressão das colunas da linha i
    print("{:3.0f}". format(matriz[i][j]), end=' ')
  print()

print()
linhas = len(matriz)
print("A matriz tem {} linhas".format(linhas))


print("A linha 1 tem {} colunas.".format(len(matriz[0])))
print("A linha 2 tem {} colunas.".format(len(matriz[1])))
print("A linha 3 tem {} colunas.".format(len(matriz[2])))