n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
s = n1 + n2

print('A soma entre {} e {} vale {}'.format(n1,n2,s))

x = input('Digite alguma coisa:')
print('O tipo primitivo desse valor é', type(x))

print('É numerico: {}' .format(x.isnumeric()))
print('É alfabetico: {}' .format(x.isalpha()))
print('É alfanumerico: {}' .format(x.isalnum()))
print('Esta em maiusculas: {}'  .format(x.isupper()))
print('Esta em minusculas: {}' .format(x.islower()))
print('É somente espaco: {}' .format(x.isspace()))
print('Esta capitalizada: {}' .format(x.istitle()))
