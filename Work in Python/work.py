lista_inteiro = [] #lista para armazenar os códigos
lista_reais = [] # lista para armazenar os saldos
print("-=-=-=-SEJA BEM-VINDO, ao \033[0;35mPINK BANK!\033[0;0m-=-=-=-")
for c in range(2):
    codigo = int(input("Informe seu CÓDIGO bancario: "))
    if codigo in lista_inteiro:
        print("ESSE CÓDIGO JÁ ESTA SENDO USADO, TENTE NOVAMENTE!")
        exit
    else:
        lista_inteiro.append(codigo)
        saldo = float(input("Informe o seu SALDO bancario R$"))
        lista_reais.append(saldo)
        print("\033[0;31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m")

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
print(lista_inteiro)
print(lista_reais)