# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0  # Inicialização da variável soma

for c in range(1, 7):
    num1 = int(input('Digite um número inteiro: '))
    if num1 % 2 == 0:
        soma += num1  # ou soma = soma + num1

print(f'A soma dos números pares é {soma}')
