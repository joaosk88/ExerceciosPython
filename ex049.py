#mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num1 = int(input('Digite um número: '))

for c in range(1, 11):  # vai de 1 até 10
    print("{} x {:2}= {}".format(num1, c, num1*c))
