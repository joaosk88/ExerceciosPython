#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: de frente para tras
frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto= ''.join(frase)
inverso = frase[::-1]

print('O inverso de {} é {}'.format(frase, inverso))

if inverso == frase:
    print('A frase é um palindromo')
else:
    print('a frase não é um palindrome')