#aqui eu coloco o tipo de conta se 1 normal se 2 universitaria
conta = int(input("Qual tipo de sua conta \n[1] Normal \n[2] Universitária \nOpção: "))
#aqui eu habilito as contas como verdadeiras para que sejam reconhecidas
conta_universitaria = True
conta_normal = True
#aqui eu crio as variaveis do saldo das contas 
saldo = 2000.0
saldo_universitario = 500.0
#aqui eu verifico se será o tipo de conta 1 ou 2, se for diferente vai dar erro
if conta == 1 or conta == 2:
    saque  = float(input("Digite o valor do seu Saque: "))
else:
    print("Transação não reconhecida, fale com seu gerente!")    
#saldo do cheque especial
cheque_especial = 450

#aqui verifico se a conta é a numero1, se for eu executo a sequencia
if conta == 1: 
    if conta_normal:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        elif saque <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial")
        else:
            print("Saque não reaizado")    
#aquieu verifico se a conta é a numero 2, e se for executo  sequencia
elif conta == 2:#se conta for igual a 2 eu executo o if abaixo
    if conta_universitaria: 
        if saldo_universitario >= saque:#se o saldo universitario for maior ou igual ao saque eu executo a sequencia abaixo
            print("Saque realizado com sucesso!")
        else:
            print("Saldo Insuficiente!")                              
            