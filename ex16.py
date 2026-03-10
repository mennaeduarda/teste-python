#Condição com AND

idade = int(input("Idade:"))
carteira = input("Tem carteira?:")

if idade >= 18 and carteira == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")