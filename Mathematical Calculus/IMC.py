### Calculando o indice de massa corporal ##

nome, altura, peso = str(input('Qual é seu nome?')), float(input('qual é a sua altura em metros (ex.: 1.80)?')), float(input('qual é o seu peso em Kg (ex.: 56)?'))

imc = (peso/(altura**2))


print(f'Olá! {nome.title()}, seu índice de massa corporal é de {imc}')