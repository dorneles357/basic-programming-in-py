## Identificador de números primos ##

num1 = int(input('Digite um inteiro positivo:'))

num = num1%2

if num == 1:
    print('numero impar')
elif num < 1:
    print('inteiros positivos deferente de zero, seu numero foi {0}'.format(num1))
else:
    print('numero par')

##Identificando números primos
num1 = int(input('digite um número:\n'))
div = 0
for i in range(1, num1 + 1):
    resto = num1 % i
    if resto == 0: 
        div = div + 1

if div == 2:
    print(f'número {num1} é primo\n')
else:
    print(f'número {num1} não é primo')

## Identificando primos:
num1 = int(input('digite um número:\n'))

for num in range(num1 + 1):
    div = 0
    for i in range(1, num + 1):
        resto = num % i
        if resto == 0: 
            div = div + 1

    if div == 2:        
        print(num)