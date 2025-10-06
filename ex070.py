print('-=' * 20)
print('LOJA SUPER BARATÃO')
print('-=' * 20)

total = 0
valor1000 = 0
menor_preco = 0
nome_mais_barato = ''
contador = 0  # Para saber se é o primeiro produto

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    contador += 1

    # Conta quantos custam mais de 1000
    if preco > 1000:
        valor1000 += 1

    # Lógica do mais barato
    if contador == 1:  # Primeiro produto
        menor_preco = preco
        nome_mais_barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_mais_barato = produto

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        print('-=' * 20)
        print('FIM DO PROGRAMA  ')
        break

print('-=' * 20)
print(f'Total da compra foi : R${total:.2f}')
print(f'Temos {valor1000} produtos custando mais de R$1.000,00')
print(f'O produto mais barato é {nome_mais_barato} que custa R${menor_preco:.2f}')
