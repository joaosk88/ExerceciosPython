
resp = 'S'
soma = quantidade = media = maior= menor= 0
while resp in 'Ss':
    num = int(input('Digite um numero'))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quantidade
print(f'voce digitou {quantidade} números e a média foi {media:.2f}')
print(f'O maior valor fo {maior} e o menor foi {menor}')
