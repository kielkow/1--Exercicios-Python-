print("Hello World")

import random
num = random.randint(0,5)
num_chute = int
print('Pensei em um número de 0 a 5, tente advinhar!')
while num_chute != num:
  num_chute = int(input('Digite o número:'))
  if num_chute == num:
    print('Parabéns, você acertou!')
  else:
    print('Putz, você errou, tente novamente!')
print('FIM DO JOGO')