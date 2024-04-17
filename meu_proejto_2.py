deposito = float(input("Digite o valor que deseja depositar: "))
saque =float(input("Digite o valor que deseja sacaar: "))
saldo = deposito - saque
limite_da_conta = deposito


if limite_da_conta == 0:
    print("Não é possivel sacar pois seu saldo é 0")
    


