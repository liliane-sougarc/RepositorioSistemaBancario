# Sistema Bancário Simples

# Variáveis para armazenar as operações
depositos = []
saques = []
saldo = 0  # Saldo inicial da conta

# Função para realizar um depósito
def depositar(valor):
    if valor > 0:  # Verifica se o valor é positivo
        depositos.append(valor)  # Adiciona o valor à lista de depósitos
        global saldo
        saldo += valor  # Atualiza o saldo
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")

# Função para realizar um saque
def sacar(valor):
    global saldo
    if len(saques) < 3:  # Verifica se já foram realizados 3 saques no dia
        if valor <= saldo and valor <= 500:  # Verifica se o saldo é suficiente e o valor não ultrapassa R$ 500,00
            saldo -= valor  # Subtrai o valor do saldo
            saques.append(valor)  # Adiciona o saque à lista de saques
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif valor > 500:
            print("Limite de saque por operação é R$ 500,00.")
        else:
            print("Saldo insuficiente!")
    else:
        print("Limite diário de saques atingido!")

# Função para exibir o extrato
def exibir_extrato():
    if depositos or saques:  # Verifica se há depósitos ou saques
        print("\nExtrato Bancário:")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo Atual: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")

# Programa principal
def menu():
    while True:
        print("\n==== Sistema Bancário ====")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(valor)
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
menu()
