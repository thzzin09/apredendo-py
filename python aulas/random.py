import random

# random de 0.0 a 1.0 float é com .random()
nm1 = random.random()
print(f"o numero sorteado foi {nm1:.2f}")

# random de numeros inteiros é com .randint()
numero = random.randint(1,10) 
print(f"o numero sorteado foi {numero}")

# random com listas é .choice()
alunos = ["pedro", "jose", "alice", "joice"]
aluno_sorteado = random .choice(alunos)
print(f"O Professor escolheu {aluno_sorteado} para limpar o quadro!!!.")

# ramdon de embaralhar a ordem de listas .shuffle()
numeros = ["pedro", 'jose', 'alice', 'joice']
random.shuffle(numeros)
print(f"A ordem dos trabalhos é : {numeros}")

#ramdon de sortear numeros em conjunto .sample(range(),)
sorteio = random.sample (range(1,51), 5)
print(f"os numeros sorteados foram {sorteio}")

