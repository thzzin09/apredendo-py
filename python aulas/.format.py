#=============================
#PROGRAMA DE CORES DO THZZIN==
#=============================
cores = {
    'limpar' : '\033[m',
    'branco' : '\033[30m',
    'vermelho' : '\033[31m',
    'verde' : '\033[32m',
    'amarelo' : '\033[33m',
    'azul' : '\033[34m',
    'roxo' : '\033[35m',
    'ciano' : '\033[36m',
    'branco' : '\033[37m'
}




n1 = int(input(f"escvreva um numero seu {cores['vermelho']}bosta{cores['limpar']} :"))
n2 = int(input(f"escvreva um numero seu {cores['ciano']}but{cores['limpar']} :"))

r =  n1 + n2

print(f"a soma corresponde a :{cores['amarelo']}{r} ")