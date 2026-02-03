n1 = float(input("escreva a primeira nota:"))
n2 = float(input("escreva a segunda nota:"))
media = (n1 + n2) /2
print(f"sua media é {media:.2}")
print("APROVADO" if media >= 6 else "REPROVADO")