import random
from time import sleep

print("JOKENPÔ")
print("Escolha sua jogada:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")

# Jogador escolhe
jogador = int(input("Digite sua opção: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

# Máquina escolhe aleatório
maquina = random.randint(0, 2)

# Mostra escolhas
opcoes = ["Pedra", "Papel", "Tesoura"]
print(f"\nJogador escolheu: {opcoes[jogador] if jogador in [0,1,2] else 'Inválido'}")
print(f"Máquina escolheu: {opcoes[maquina]}")

# Regras do jogo
if maquina == 0:  # Máquina jogou Pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCEU")
    elif jogador == 2:
        print("MÁQUINA VENCEU")
    else:
        print("Jogada inválida")

elif maquina == 1:  # Máquina jogou Papel
    if jogador == 0:
        print("MÁQUINA VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("Jogada inválida")

elif maquina == 2:  # Máquina jogou Tesoura
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("MÁQUINA VENCEU")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida")
