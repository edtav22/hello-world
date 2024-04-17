saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
    
if saldo < saque:
    print("Saldo insuficiente!")
    print("Volte a tela principal!")
else:
    print("Fim") 

opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato \nOpção: "))                

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    print("Realizando saque")
elif opcao == 2:
    print("Exibindo o Extrato")
else:
    print("Opção Inválida")
    
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH!")
    
if idade < 18:        
    print("Não pode tirar a CNH")
    
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
else:
    print("Não pode tirar CNH")
    
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não praaticas")
else:
    print("Ainda não pode tirar CNH")             