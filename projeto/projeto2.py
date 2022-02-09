# Projeto 02 - Chute um número

# importando biblioteca random
from random import randint

#Gerando um valor aleatorio entre 1 e 10
valor_aleatorio = randint(1,10)

#Verificando o valor aleatorio gerado
print(valor_aleatorio)

#Informando o chute do número do usuário
chute = int(input("Chute um número de 1 a 10: "))
acertou = False

#Executando até que o número chutado seja o correto
while acertou == False:
  if valor_aleatorio == chute :
      acertou == True
      print("Você acertou!")
      break
  elif  chute < valor_aleatorio :
      print ("O valor chutado é menor que o valor gerado!")
      chute = int(input("Chute um número de 1 a 10: "))
  else:
    print ("O valor chutado é maior que o valor gerado!")
    chute = int(input("Chute um número de 1 a 10: "))
