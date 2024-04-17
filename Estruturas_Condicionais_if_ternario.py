saldo = 2000.0
saque = float(input("Digite o valor do seu saque: "))

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")