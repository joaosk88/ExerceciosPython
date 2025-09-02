# crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
from shlex import split

nome = str(input('Digite seu nome completo: ')).strip()
nome.split(nome)
print( 'Seu nome tem silva? {}'.format('silva' in nome.lower())) # in não é um metodo é um operador do python