nt1 = float(input("escreva a primeira nota :"))
nt2 = float(input("escreva a segunda nota :"))
nt3 = float(input("escreva a terceira nota :"))
nt4 = float(input("escreva a quarta nota :"))
if nt1 > 10 or nt2 > 10 or nt3 >  10 or nt4 > 10:
    print("certeza que digitou a nota certa? o maximo é 10.0 por nota") 
else: 
    media = (nt1 + nt2 + nt3 + nt4) / 4
    print("A media das notas é equivalente a :{}" .format (media))