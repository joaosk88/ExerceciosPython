#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont =('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','quatorze','quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    valor=int(input('Digite um número entre 0 e 20: '))
    if 0 <= valor <= 20:
        break
    print(f'O valor digitado foi {cont[valor]}')
    escolha= str (input('Deseja continuar? [S/N]: '))
    if escolha == 'S':
        valor = int(input('Digite um número entre 0 e 20: '))
    if escolha == 'N':
        print('Programa finalizado')
        break
    
print(f'O valor digitado foi {cont[valor]}')


