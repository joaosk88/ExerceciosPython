#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = 0
cont = 0

# loop infinito até break
while True:
    n = int(input('Digite um número [999 para parar]: '))

    # se for 999, sai do loop
    if n == 999:
        break

    # senão, soma e conta
    soma += n
    cont += 1

# depois do loop, exibe os resultados
print(f'Você digitou {cont} números e a soma foi {soma}.')
