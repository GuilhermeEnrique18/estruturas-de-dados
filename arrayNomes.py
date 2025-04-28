arrayNomes = ["","","","",""]
for i in range(len(arrayNomes)):
    arrayNomes[i]= input(f"Informe o nome {i + 1}: ")
for i in range(len(arrayNomes)):
    print(f"{arrayNomes[i]} esta na posição - {i}")