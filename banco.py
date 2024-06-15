menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""


saldo = 0
saque = 0
limite = 500
LIMITE_SAQUE = 3
quantidade_saque = 0

extrato = ""


def depositar():
    global saldo
    val_deposito = int(input("Informe o valor que quer depositar: R$"))
    saldo = saldo + val_deposito
    print(
        f"Você depositou o valor de: R${val_deposito}\n Seu saldo agora é de: R${saldo}"
    )


def sacar(val_saque):
    global saldo, quantidade_saque

    if quantidade_saque >= LIMITE_SAQUE:
        print("Quantidade de saque excedida, você já fez 3 saques hoje")

    elif val_saque > limite:
        print("O limite de saque é de até R$ 500 reais")

    elif val_saque > saldo:
        print(
            f"Saldo Insuficiente, seu saldo atual é de: R$ {saldo}\n Informe um valor menor ou igual ao seu saldo"
        )
    else:
        quantidade_saque += 1
        saldo = saldo - val_saque
        print(f"Você sacou: R${val_saque}\n Sei novo saldo é de {saldo}")


def imprime_extrato():
    global extrato, quantidade_saque, saldo, saque

    extrato = f"""
        Seu saldo é de R${saldo}

        Seu número de saques hoje é de {quantidade_saque}

        Você pode sacar até {LIMITE_SAQUE - quantidade_saque} vezes hoje
        
        Ultimo saque seu foi de: R${saque}

        """
    print(extrato)


while True:
    print("--- Escolha uma opção ---")
    opcao = input(menu)

    if opcao.lower() == "d":
        depositar()

    elif opcao.lower() == "s":
        saque = int(input("Informe o valor que deseja sacar: R$"))
        sacar(saque)

    elif opcao.lower() == "e":
        imprime_extrato()

    elif opcao.lower() == "q":
        print("Encerrando transação, obrigado e volte sempre!")
        break

    else:
        print("Opção invalida, por favor selecionem novamente a opção desejada.")
