# Lista de bandas e contadores de votos
bandas = ["Banda Solar", "Fúria Sonora", "Eclipse Azul", "Os Encantados", "Ressonância"]
votos = [0, 0, 0, 0, 0]

print("Eleição da Melhor Banda do Festival")
print("Vote digitando um número de 1 a 5:")
print("1 - Banda Solar")
print("2 - Fúria Sonora")
print("3 - Eclipse Azul")
print("4 - Os Encantados")
print("5 - Ressonância")
print("Digite 0 para encerrar. Máximo de 99 votos.")

total_votos = 0

# Coleta dos votos
while total_votos < 99:
    voto = int(input("Seu voto: "))

    if voto == 0:
        print("Encerrando a votação.")
        break

    if voto < 1 or voto > 5:
        print("Voto inválido. Tente novamente.")
        continue

    votos[voto - 1] = votos[voto - 1] + 1
    total_votos = total_votos + 1

# Verifica se houve votos
if total_votos == 0:
    print("Nenhum voto registrado.")
else:
    print("\nResultado final da votação:")
    for i in range(5):
        porcentagem = (votos[i] * 100) / total_votos
        print(bandas[i], "-", votos[i], "votos -", round(porcentagem, 1), "%")

# Identificação do maior número de votos das bandasss
maior = votos[0]
for i in range(1, 5):
    if votos[i] > maior:
        maior = votos[i]

# Verifica empate
empatadas = []
for i in range(5):
    if votos[i] == maior:
        empatadas.append(i)

# Resultado final
if len(empatadas) == 1:
    print("\nA banda vencedora é:", bandas[empatadas[0]])
else:
    print("\nEmpate entre as bandas:")
    for i in empatadas:
        print("-", bandas[i])

#jogo de impar ou par para decidir a banda ganhadora!! uhuuul arrasame
if len(empatadas) == 1:
    vencedora = empatadas[0]

print("\nVamos desempatar com um jogo de Ímpar ou Par!")
print("Você escolhe Ímpar (1) ou Par (2)")

escolha = int(input("Digite 1 para Ímpar ou 2 para Par: "))

numero_usuario = int(input("Digite um número entre 1 e 10: "))

print("Número escolhido pelo usuário: 6")
soma = numero_usuario + 6

if soma % 2 == 0:
    resultado = 2 # Par
else:
    resultado = 1 # Ímpar

if escolha == resultado:
    vencedora = empatadas[0]
else:
  vencedora = empatadas[1 % len(empatadas)]
  print("\nA banda vencedora após o desempate é:", bandas[vencedora])