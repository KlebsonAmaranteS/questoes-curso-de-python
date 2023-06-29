from random import randint
from time import sleep
pc = randint(0,5)
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 20)

user = int(input("Em que número pensei? "))

print('PROCESSANDO...')
sleep(3)

if pc == user:
    print("PARABÉNS, você venceu!")
else:
    print(f"GANHEI, eu pensei no número {pc} e não no {user}.")