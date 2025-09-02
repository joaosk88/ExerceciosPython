#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente ex ( ANA MARIA DE SOUZA_ primeiro= ana último= souza
nome = str(input('Digite seu nome completo')) .strip()

print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu ultimo nome é {}'.format(nome.split()[len(nome.split())-1]))