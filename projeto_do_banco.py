menu = """

[1] Depositar 
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("Depósito") 
        valor = float(input("Iforme o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inv´lido.")
            
    elif opcao == "2":
        print("Sacar")
        valor = float(input("Informe o valor do saque: "))
    
        excedeu_saldo = valor > saldo 
    
        excedeu_limite = valor > limite
    
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Você não tem saldo suficiente.")    
        
        elif excedeu_saques:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")    
            
    elif opcao == "3":
        print("Extrato")
        print("\n=============== EXTRATO ===============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
                
    elif opcao == "4":
        print("Sair")    
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")