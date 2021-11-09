# Exemplo 2
# definição de uma função que realiza a leitura
# de um inteiro e o retorna
def Le():
  return int(input("digite um inteiro: "))

a = Le() # primeira chamada à função Le()
b = Le() # segunda chamada à função Le()

r = a**b
print("{} elevado a {} é {}".format(a, b, r))