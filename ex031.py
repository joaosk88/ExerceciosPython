#definir um valor que sera gasto dependendo da distancia em kms
viagem = int(input('Qual a distâmcoa da sua viagem? '))

v1 =  (0.50 * viagem)
v2 = (0.45 * viagem)

if viagem <= 200:
    print('kms percorrido: {} Viagem economica o valor é R${:.2f}'.format(viagem, v1))

else:
    print('Kms percorrido: {} Viagem longa o valor é R${:.2f}'.format(viagem, v2))

