## Calculando o seno e coseno 
co = float(input('\nInforme o cateto oposto ao ângulo:'))
ca = float(input('\nInforme o cateto adjacente ao ângulo:'))

h = (co*co + ca*ca)**(0.5)
angsen = co/h
angcos = ca/h

print(f'O ângulo seno é {angsen} e o cosseno é {angcos}')