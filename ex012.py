#leia o item e aplique 5% de desconto
item = float(input('Qual o valor do produto? R$'))
promo =  item - (item * 5/100)
print('O produto que custava R${}, na promoção com desconto de 5% sai por R${:.2f}'.format(item, promo))