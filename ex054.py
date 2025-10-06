#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):  # Vai de 1 até 7
    nascimento = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = atual - nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print()
print(f"Ao todo obtivemos {maiores} pessoas maiores de idade.")
print(f"E também tivemos {menores} pessoas menores de idade.")
