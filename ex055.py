#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []  # lista vazia para guardar os pesos

for i in range(1, 6):  # Vai de 1 até 5
    peso = float(input(f'Peso da {i}ª pessoa: '))
    pesos.append(peso)  # adiciona o peso na lista

# Mostra o maior e o menor
print("O maior peso foi:", max(pesos))
print("O menor peso foi:", min(pesos))

