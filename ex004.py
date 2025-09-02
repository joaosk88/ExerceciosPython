
a = input('Digite algo ') #aqui entramos com o dado
print('Tipo de dado',type(a)) #nesse caso sempre vai retornar como string pois eu nao coloquei o tipo primitivo que representa a variavel (a)

print('Tem espaços?',a.isspace())# aqui vemos se tem espaço
print('É um numero?',a.isalnum())# aqui vemos se o input digitado é um numero ex1
print('Contém  letras?',a.isalpha()) #aqui vemos se são letras
print ('É um alfanumerico?',a.isnumeric()) #aqui vemos se é um alfanumerico
print ('Tem letras maiusculas?',a.isupper()) #aqui vemos se tem letras maiuculas
print ('Tem letras minusculas?',a.islower()) #aqui vemos se tem letras minusculas
print ('Esta capitalizada?',a.capitalize())  # aqui vemos se esta capitalizada
