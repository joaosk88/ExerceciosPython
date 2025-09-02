from random import choice, randint
from time import sleep

print('-=-'* 20)
print('____Vou pensar em um número de 1 a 5, tente advinhar____ ')
print('-=-'* 20)
#primeiro jeito que consegui fazer
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n1, n2, n3, n4]
sorteio = choice([n1, n2, n3, n4, n5])
n1 = int(input('Digite um numero:'))
print('PROCESSANDO...')
sleep(2)
if n1 == sorteio:
    print('Parabéns você acertou o numero {}'.format(sorteio))
else:
    print('voce errou')

print('o Numero sorteado foi {}'.format(sorteio))


#jeito expicado em aula
computer = randint(1,5) #o computador vai escolher um numero aleatorio entre 1 e 5
print('-=-'* 20)
print('____Vou pensar em um número de 1 a 5, tente advinhar____ ')
print('-=-'* 20)

jogador = int(input('Qual numero sorteado:'))
print('PROCESSANDO...')
sleep(2)
if jogador == computer:
    print('Parabén você venceu')
else:
    print('Voce perdeu')
