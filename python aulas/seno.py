import math

x = float(input("escreva o valor do angulo que você quer descobir :"))
rad = math.radians(x)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f"O valor do angulo {x:.0f}° convertido é :")
print(f"Seno = {sen:.2f}")
print(f"Coseno = {cos:.2f}")
print(f"Tanjente = {tan:.2f}")



