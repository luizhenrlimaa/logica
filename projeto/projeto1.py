# Projeto 01 - Fatorial de um número

# Pegando um número do usu
numero = int(input("Informe um número: "))
# O número deve ser positivo
if numero > 0:
  fatorial = 1
# Calculando o fatorial
  for item in range(1, numero+1):
    fatorial = fatorial*item
  print(fatorial)