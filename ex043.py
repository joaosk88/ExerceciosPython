"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input("Qual seu peso? (KG)"))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2)

print('O IMC  dessa pessoa é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Voce esta abaixo do peso NORMAL!')
elif imc <=25:
    print('PARABÉNS, Voce esta com o peso ideal!')
elif imc <= 30:
    print ('Voce esta com sobrepeso!')
elif imc <= 40:
    print('Voce esta com obesidade!')

else:
    print("Obesidade Mórbida")