#receba um numero do teclado e exiba os 2 numeros seguintes
a = int(input("Informe um numero inteiro: "))
print(a)
#repita duas vezes 
a += 1
print(a)
a += 1
print(a)
#essa forma acima é sem o comandoo de repetição

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
#aqui ele procura as letras que eu escrevi na palavra e se encontrar alguma vogal salva na variavel letra
for letra in texto:
    if letra.upper() in VOGAIS:#aqui ele coloca tudo da variavel letra em maiuscula, e procurade tem alguma igual
        print(letra, end="")#aqui exibo as letras encontradas uma a uma
else:
    print()#adiciona a quebra de linha
    print("Executa no final do laço")        

#função range
for numero in range(0, 11):
    print(numero, end="")
    print()
#exibindo a tabuada de 5    
for numero in range(0, 51, 5):
    print(numero, end="")    
    print()
    
for numero in list(range(10)):
    print(numero, end="")    