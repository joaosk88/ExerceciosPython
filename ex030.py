# criar um programa que informa se o numero digitado é impar ou par

numero = int(input('Insira um numero: '))

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é PAR"
    else:
        return f"{numero} é ÍMPAR"

# chamada da função e exibição do resultado
print(par_ou_impar(numero))
