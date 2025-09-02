#faça um programa que lçeia tres numeros e mostre qual é o maior deles

n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))
n3 = int(input('Digite o terceiro numero '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)


print("Maior número: {maior}")
print("Menor número: {menor}")