preco = float(input("digite o preço do seu produto :"))
porcentagem = float(input("digite o desconto do produto :"))

totalp = preco * (porcentagem / 100)
totalr = preco - totalp

print(f"o desconto do seu produto é igual a : {totalr}")