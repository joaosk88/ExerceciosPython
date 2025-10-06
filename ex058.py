'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import choice, randint

computer = randint(1,10) #o computador vai escolher um numero aleatorio entre 1 e 10
print('sou seu computador ...')
print('acabe de pensar em numero entre 1 e 10')

palpites = 0
acertou = False

while not acertou:
    jogador= int(input('Qual é seu palpite?' ))
    palpites += 1
    if  jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('Mais... Tente outra vez')
        elif jogador > computer:
            print('Menos... Tente outra vez')
print(f'Acertou com {palpites} tentativas, Parabéns!')
