import random
vlct = random.randrange(80, 180)
ys = input("quer ver sua velocidade? y/n :")
print(f"a sua velocidade foi de {vlct}km/h" if ys == "y"  else "Tudo bem, tenha um bom dia ")
if vlct > 100:
    excesso = vlct - 100
    multa = excesso * 7
    print("sua velocidade foi acima do permitido pela via, VOCÊ TOMOU UMA MULTA SEU BOBOCA!!!")
    print(f"o valor da sua multa é de R${multa} ")
else:
    print("Tenha um otimo dia")
