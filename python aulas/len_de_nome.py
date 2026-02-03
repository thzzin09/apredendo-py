nome = input("Digite seu nome aqui :")

maisc =  nome.strip().upper()
print(f"Seu nome com letras maiusculas fica :{maisc}")

minus =  nome.strip().lower()
print(f"Seu nome com letras minusculas fica :{minus}")

nospace = len(nome.strip().replace(' ' , ''))
 
print(f'Seu nome tem um total de : {nospace} letras contando com o espaço do meio.')

nm1 =  nome.split()
nome = nm1[0]
primnm = len(nm1[0])
print(f"o seu primeiro nome tem {primnm} letras")



