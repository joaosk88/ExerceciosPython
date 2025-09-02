#leia altura e largura de uma parede para saber quantos litros de tinta precisa para a mesma ser pintada

altura=  float(input('Digite a altura:'))
largura= float(input('Digite a largura:'))
area= altura*largura

print ('Sua parede tem uma dimensão de {} x {} e sua área é de {:.3f}m²'.format(altura, largura, area))

tinta = area/2

print('Para pintar essa parede você precisa de {:.3f}L de tinta'.format(tinta))
