import random

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
    'ciano' : '\033[46m',
    'branco' : '\033[37m'

}


nm = random.randint(1,5)
nmu = int(input(f"digite o numero que vc acha q eu estou {cores['ciano']}pensando{cores['limpar']} de {cores['vermelho']}1{cores['limpar']} a {cores['azul']}5 {cores['limpar']} :"))
if nmu == nm:
    print(f"você {cores['verde']}ACERTOU!!!!{cores['limpar']}")
else:
    print(f"você {cores['vermelho']}ERROU HAHA!!{cores['limpar']}")