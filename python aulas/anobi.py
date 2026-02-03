ano = int(input("escreva o ano que você quer descobrir :"))
anobi = (ano % 100) % 4
if anobi > 0:
    print("esse ano não é Bissexto!!")
else:
    print("esse ano é bissexto!!")


