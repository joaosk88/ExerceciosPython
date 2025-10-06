#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitoria = 0

print('VAMOS JOGAR UM JOGO')

while True:
    maquina = randint(0, 10)  # número inteiro entre 1 e 10 (inclui 1 e 10)
    jogador = int(input('Diga um valor:'))
    total = maquina + jogador
    tipo = ' '
    while tipo not in 'PIpi':
        tipo = str(input('Par ou impar? [P/I] ')).upper()[0]
    print(f'Você jogou {jogador} e o computador {maquina} total de  {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR' if total %2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if jogador % 2 == 0:
            print('Você venceu')
            vitoria += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if jogador % 2 == 1:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print (f'GAME OVER! vitorias: {vitoria}')




