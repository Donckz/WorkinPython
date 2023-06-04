def realizar_deposito(codigos, saldos):
    codigo = int(input("Digite o código da conta: "))
    if codigo in codigos:
        indice = codigos.index(codigo)
        valor = float(input("Digite o valor a ser depositado: "))
        saldos[indice] += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")

def realizar_saque(codigos, saldos):
    codigo = int(input("Digite o código da conta: "))
    if codigo in codigos:
        indice = codigos.index(codigo)
        valor = float(input("Digite o valor a ser sacado: "))
        if saldos[indice] >= valor:
            saldos[indice] -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

def consultar_ativo_bancario(saldos):
    total = sum(saldos)
    print("Ativo bancário: R$ {:.2f}".format(total))

def main():
    codigos = []
    saldos = []

    for _ in range(2):
        codigo = int(input("Digite o código da conta: "))
        if codigo in codigos:
            print("Código já cadastrado. Digite outro código.")
            continue
        saldo = float(input("Digite o saldo da conta: "))
        codigos.append(codigo)
        saldos.append(saldo)

    while True:
        print("\nMenu:")
        print("1. Realizar Depósito")
        print("2. Realizar Saque")
        print("3. Consultar o ativo bancário")
        print("4. Finalizar Programa")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            realizar_deposito(codigos, saldos)
        elif opcao == 2:
            realizar_saque(codigos, saldos)
        elif opcao == 3:
            consultar_ativo_bancario(saldos)
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Digite novamente.")

    print("Programa finalizado.")


if __name__ == "__main__":
    main()