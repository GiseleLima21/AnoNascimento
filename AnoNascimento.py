import os
os.system("clear") or None

print("Este progama informa o ano do seu\nnascimento")
ano   = int(input ("Qual o ano atual? "))
idade = int(input ("Qual a sua idade? "))
resul = ano - idade
print("Você nasceu em", resul)