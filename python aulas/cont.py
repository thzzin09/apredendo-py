cont = input("ESCREVA uma frase:")
cont1 =cont.count('a')
cont2 =cont.count('A')
total = cont1 + cont2
print(f'a letra a aparece {total} vezes na frase')
ps1 = cont.lower().find('a') + 1
ps2 = cont.lower().rfind('a') + 1
print(f'a primeira letra "A" aparece na posição {ps1}')
print(f'a ultima letra a aparece na posição {ps2}')