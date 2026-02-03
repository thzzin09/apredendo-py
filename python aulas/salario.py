sal = float(input('digite seu salario :'))
if sal >= 1250:
    aumento = (sal * 0.1)
    run =(sal + aumento)
    print(f'seu salario teve um aumento de 10%, o valor total agora é de :R${run:.2f}')
else:
    aumento2 = (sal * 0.15)
    run2 = (sal + aumento2)
    print(f'seu salario teve um aumento de 15%, o valor total agora é de :R${run2:.2f}')
print('-><-' *20)
print('>>>>>FIM<<<<<')