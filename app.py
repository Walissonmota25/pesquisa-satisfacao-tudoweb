# Pesquisa de satisfação da empresa TudoWeb

# Define a quantidade de entrevistados
quantidade_entrevistados = 50

# Cria os contadores das respostas
excelente = 0
ruim = 0

print("======================================")
print("     PESQUISA DE SATISFAÇÃO TUDOWEB")
print("======================================")

# Repetição para realizar a pesquisa com os entrevistados
for i in range(quantidade_entrevistados):

    print(f"\n--- Entrevistado {i + 1} de {quantidade_entrevistados} ---")

    # Solicita os dados do entrevistado
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    # Solicita a opinião sobre o atendimento
    print("\nOpções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção: "))

    # Verifica a opinião utilizando estrutura de decisão
    if opiniao == 1:
        excelente += 1
        resposta = "EXCELENTE"

    elif opiniao == 2:
        resposta = "BOM"

    elif opiniao == 3:
        ruim += 1
        resposta = "RUIM"

    else:
        resposta = "OPÇÃO INVÁLIDA"

    # Exibe o retorno da pesquisa
    print(f"\nEntrevistado: {nome}")
    print(f"Idade: {idade}")
    print(f"Opinião: {resposta}")

# Exibe o resultado final da pesquisa
print("\n======================================")
print("          RESULTADO DA PESQUISA")
print("======================================")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")