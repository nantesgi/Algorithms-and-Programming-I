# Exemplo 8

# função que lê e retorna um inteiro
def LeInteiro():
  return int(input())


# função que realiza a validação de um dado de entrada
# caso o valor de i seja menor que m e maior que n, 
# esta função retorna False, caso contrário retorna True
def Valida(i, inferior, superior):
  if (i < inferior) or (i > superior):
    return False
  else:
    return True

# função que lê uma lista L de m valores inteiros (correspondente a uma linha da matriz)
def LeLinha(n, L):
  for j in range(n):
    L.append(int(input()))


# função que imprime uma linha i da matriz M que possui n colunas
#def ImprimeLinha(M, n, i):

#função que imprime uma coluna j da matriz M que possui m linhas
#def ImprimeColuna(M, m, j):

#######################
# Corpo principal
#######################
matriz = []

while True:
  print("Digite a quantidade de linhas: ")
  m = LeInteiro()
  v = Valida(m, 0, 13)
  if v == True:
    break
  else:
    print("Opa. A dimensão da matriz não pode ser superior a 13x25")

while True:
  print("Digite a quantidade de colunas: ")
  n = LeInteiro()
  v = Valida(m, 0, 25)
  if v == True:
    break
  else:
    print("Opa. A dimensão da matriz não pode ser superior a 13x25")

for i in range(m):
  linha = []
  print("Digite os valores da linha {} (separados por enter)".format(i+1))
  LeLinha(n, linha)
  matriz.append(linha)

print(matriz)