nome = "EDmAr"
#letras todas maiusculas
print(nome.upper())
#letras todas minusculas
print(nome.lower())
#primeira letra maiuscula
print(nome.title())

texto = "   Olá Mundo  "
#remove todos os espaços
print(texto.strip())
#remove os espaços da esquerda
print(texto.lstrip())
#removeos espaços da direita
print(texto.rstrip())

menu = "Python"
menu1 = "Java"

print("####" + menu + "####", "####" + menu1 + "####")
print(menu.center(14), menu1.center(14) )
print(menu.center(14, "#"))
print("P-y-t-h-o-n")

for letra in menu:
    print(letra, end="-")
    
print()    
print("-".join(menu))    
    

