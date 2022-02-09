# Projeto 02 - Medidor de Velocidade

#Valor da velocidade máxima
velocidade_maxima = 80

#Informando o valor da velocidade
velocidade = int(input('Informe a velocidade: '))

# Comparando os valores da velocidade e exibindo o resultado
if (velocidade <= velocidade_maxima):
   print('Não houve multa!')
elif (velocidade - velocidade_maxima) <= 10 and (velocidade - velocidade_maxima) > 0:
    print('Multa leve!')
elif (velocidade - velocidade_maxima) > 10 and (velocidade - velocidade_maxima) <= 20:
    print('Multa grave!')
else:
    print("Multa gravissíma!")