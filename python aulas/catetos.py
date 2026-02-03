import math

n1 = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto adjacente: '))
hp =  math.hypot(n1, n2) 
print(f'O comprimento da hipotenusa é de : {hp:.3f}')
# hypot calcula a hipotenusa
# math é a biblioteca de funções matemáticas
# import math importa a biblioteca math
# from math import hypot importa apenas a função hypot da biblioteca math
# import math as mt importa a biblioteca math com um apelido (mt)
# from math import sqrt as raiz importa a função sqrt da biblioteca math com um apelido (raiz)
# sqrt calcula a raiz quadrada