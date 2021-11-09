# Exemplo 7

# recebe uma lista de inteiros e remove o menor elemento desta lista
def remove_minimo(lista):
  
  iMenor = 0;

  # encontra a posição do menor elemento
  for i in range(1, len(lista)):
    if lista[i] < lista[iMenor]:
      iMenor = i

  # desloca todos os elementos que estão
  # a direita do menor elemento, uma 
  # posição à esquerda
  for i in range(iMenor, len(lista)-1):
    lista[i] = lista[i+1]

  
# lê vários inteiros em uma única linha e os armazena em 
# uma lista 
l = list(map(int,input().split()))

# remove o menor elemento da lista
removeMinimo(l)

for i in range(len(l)-1):
  print(l[i], end= ' ')