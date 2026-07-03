#Jogo de adivinhação, treinando programação.
import random

numero_secreto = random.randint(1,10)

acertou = False

while not acertou:
    palpite = int(input('Tente advinhar o número (1 a 10):'))

    if palpite == numero_secreto:
        print('Parabéns, você acertou!')
        acertou = True
    else:
        if palpite < numero_secreto:
            print('O número é maior.')
        else:
            print('O número é menor.')
print('Fim do jogo! O número secreto era {}.'.format(numero_secreto))