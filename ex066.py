#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n= s =  0
cont = 0
while True:
    n = int(input('Insira um numero (999 para parar): '))

    if n ==999:
        break
    s += n
    cont += 1
print(f'A soma vale {s} e foram digitados {cont} numeros')