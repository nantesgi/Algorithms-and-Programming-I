# Exemplo 4

# lendo matriz do teclado (lendo por linhas!)
matriz = []

# validação de dado de entrada
while True:
  print("Quantas linhas tem a sua matriz?")
  linhas = int(input())
  if(linhas > 0):
    break; # finaliza o while infinito (while True)

# temos um n positivo!!!

print("Digite os elemento da matriz, linha a linha")

# linhas == 3

# lendo a matriz, linha a linha
for i in range(linhas): #i = 0, 1, 2
    #lista de elemento que correspondem a linha i
    linha = [] # variável auxiliar para guardar a lista lida na entrada (linha da matriz)
    print("elementos da linha %d: " %(i+1), end='')
    linha = list(map(int, input().split())) # temos uma lista!

    #adicionando uma nova linha à matriz
    matriz.append(linha)

    #print(matriz[i])
    #matriz.append(list(map(int, input().split())))

# ex.: linhas == 3
# i é o controle da linha a ser visitada
i = 0 ##### condição inicial
while i < linhas: ### condição de parada
  i += 1 ###### incremento
  # já que estamos na linha i, temos que visitar todos os elementos desta linha (colunas!)
  j = 0
  while j < len(matriz[i]): # len(matriz[i]) retorna a quantidade de elementos (colunas!) da linha i
    # i e j representam o que?
    print(matriz[i][j], end='')
    j += 1
  print()
  

for linha_que_eu_quero in range(linhas): 
  for coluna_que_eu_quero in range(len(matriz[linha_que_eu_quero])): # impressão das colunas da linha i
    print("{:6.0f}". format(matriz[linha_que_eu_quero][coluna_que_eu_quero]), end=' ')
  print()