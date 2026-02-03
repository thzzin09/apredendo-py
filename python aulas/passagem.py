dis = float(input("DIGITE a distancia da sua VIAGEM em KM :"))
print(f"===>>>{dis:.2f}KM<<<===")
if dis > 200:
    preco = (dis * 0.5)
    print(f"Como sua DISTANCIA é acima de 200km o preço da sua passagem é de R${preco:.2f}!!")
else:
    precoD = (dis * 0.45)
    print(f"O preço da sua passagem é de R${precoD:.2f}!!")
print("Tenha uma otima viagem!!!")

