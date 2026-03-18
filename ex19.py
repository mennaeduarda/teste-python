#Prioridade
age = int(input("Idade:"))
pregnant = input("É gestante? (sim ou não):")

if age >= 60 or pregnant == "Sim":
    print("Atendimento preferencial.")
else:
    print("Atendimento normal.")
