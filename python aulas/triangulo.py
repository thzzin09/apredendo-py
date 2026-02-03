print('=-' * 20)
print('ANALISADOR DE TRIANGULOS')
print('=-' *20)
rt1 = float(input('digite o valor da prmeira reta do triangulo :'))
rt2 = float(input('digite o valor da segunda reta do triangulo :'))
rt3 = float(input('digite o valor da terceira reta do triangulo :'))


if (rt1 + rt2 > rt3) and (rt2 + rt3 > rt1) and (rt3 +rt1 > rt2):
    print(' PODEM FORAMR UM TRIANGULO')
else:
    print('NÃO FORMAM UM TRIANGULO') 

