notas = [0.0,0.0,0.0,0.0,0.0]
n = 0
alunosAcima = 0
for i in range (len(notas)):
    notas[i]= float(input(f"Digite a nota {i + 1}: "))

for i in range (len(notas)):
    n = n + notas[i]

media = n / len(notas)

for i in range (len(notas)):
    if notas[i] > media:
       alunosAcima+=1
        
print(f"A media da sala é: {media:.2f}. {alunosAcima} ficaram acima da média. ")