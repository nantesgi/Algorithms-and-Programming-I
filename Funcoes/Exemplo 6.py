# Exemplo 6 

# definição de uma função que realiza a leitura
# de um inteiro e o retorna
def Le():
  return int(input("digite um inteiro: "))

# definição da função de calcula o valor de x**y
#esta função possui dois parâmetros de entrada
def Potencia(a, b):
  resultado = a**b
  # modificando o valor da variável local a
  a = a*3
  # modificando o valor da variável local b
  b = b*3
  print("Valor da variável a (local à função Potencia):", a)
  print("Valor da variável b (local à função Potencia):", b)
  return resultado

# início da função principal - main()
a = Le()
b = Le()
r = Potencia(a,b)
print("\nValor da variável a (local à função principal):", a)
print("Valor da variável b (local à função principal):", b)
  
print("\n{} elevado a {} é {}".format(a, b, r))