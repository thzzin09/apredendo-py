nm1= float(input('escreva o primeiro numero :'))
nm2= float(input('escreva o segundo numero :'))
nm3= float(input('escreva o terceiro numero :'))

if nm1 > nm2 and nm1 > nm3:
    print(f'o maior numero é :{nm1}')
elif nm2 > nm1 and nm2 > nm3:
    print(f'o maior numero é :{nm2}')
elif nm3 > nm1 and nm3 > nm2:
    print(f'o maior numero é :{nm3}')
if nm1 < nm2 and nm1 < nm3:
    print(f'o menor numero é :{nm1}')
elif nm2 < nm1 and nm2 < nm3:
    print(f'o menor numero é :{nm2}')
elif nm3 < nm1 and nm3 < nm2:
    print(f'o menor numero é :{nm3}')


print('FIM!!!')
