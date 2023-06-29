import random

def usuario_escolhe_jokenpo():
    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
        if escolha_usuario in ['pedra', 'papel', 'tesoura']:
            return escolha_usuario
        else:
            print("Opção inválida! Tente novamente.")

def computador_escolhe_jokenpo():
    sortear = ['pedra', 'papel', 'tesoura']
    return random.choice(sortear)

def determina_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or (escolha_usuario == 'papel' and escolha_computador == 'pedra') or (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        return "Você venceu!"
    else:
        return "Eu venci!"

def jogar_novamente():
    jogar_de_novo = input("Deseja jogar novamente? (s/n): ").lower()
    return jogar_de_novo == 's'

def jogar_jokenpo():
    print("Bem-vindo ao Jokenpô!")
    while True:
        escolha_usuario = usuario_escolhe_jokenpo()
        escolha_computador = computador_escolhe_jokenpo()
      
        print(f"\nVocê escolheu: {escolha_usuario}")
        print(f"Eu escolho: {escolha_computador}\n")
        
        resultado = determina_vencedor(escolha_usuario, escolha_computador)
        print(resultado)
        
        if not jogar_novamente():
            break

jogar_jokenpo()
