
## Calculadora de salário ##
nome, idade =  str(input('Qual é o seu nome?')) , int(input('Qual a sua idade?')) 

salario, imposto = int(input('Qual é o seu salário?')), float(input('Qual é o imposto cobrado em decimal (ex.: 0.34)?'))

print(f'Olá! {nome.title()}, você nasceu em {2020 - idade} e o valor real de seu salário é {salario - (salario*imposto)}')

if imposto < 10.:
    print("Baixo")
elif imposto >= 10. and imposto <= 27.:
    print("Médio")
elif imposto > 27. and imposto < 100:
    print("Alto")
else:
    print("Imposto inválido")

'''
salario = int(input('salario?'))
imposto = 27
while imposto > 0.:
    imposto = input('imposto ou (0) para sair')
    if not imposto:
        imposto =27
    else:
        imposto = float(imposto)
    
    print(f'valor real: {(salario - (salario*imposto*0.01))}')
'''








