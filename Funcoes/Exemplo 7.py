# Exemplo 7

# podemos também definir a função principal do nosso scrit que por padrão é chamada de main(). Veja:

# definição de uma função que realiza a leitura
# de um inteiro e o retorna
def Le():
  return int(input("digite um inteiro: "))

# definição da função de calcula o valor de x**y
# esta função possui dois parâmetros de entrada
def Potencia(a, b):
  resultado = a**b
  return resultado



# definição da função principal
def main():
  a = Le()
  b = Le()
  r = Potencia(a,b)
  print("{} elevado a {} é {}".format(a, b, r))


# chamada à função principal
main()