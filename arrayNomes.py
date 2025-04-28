arrayNomes = ["",""]
for i in range(len(arrayNomes)):
    arrayNomes[i]= input(f"Informe o nome {i}: ")
nome = input("Digite o nome para saber se esta na lista: ")

if nome in arrayNomes:
    print(nome, "Na posição", [i])

else:
    print("Não está")