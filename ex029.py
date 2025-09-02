print('-=-' * 20)
print('RADAR ELETRONICO PYTHON')
print('-=-' * 20)

v1 = float(input('Qual é a velocidade atual do carro?: '))

limite = 80

if v1 > limite:
    multa = (v1 - limite) * 7  # cálculo da multa
    print(f'Você foi multado! Valor da multa: R${multa}')
else:
    print('boa viagem')
