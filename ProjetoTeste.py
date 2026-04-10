#cálculo de média de notas
N1 = float(input("digite a primeira nota: "))
N2 = float(input("digite a segunda nota: "))
N3 = float(input("digite a terceira nota: "))
N4 = float(input("digite a quarta nota: "))
media = (N1 + N2 + N3 + N4 ) / 4

#caso de média maior ou menor que 7, ou seja, aprovado ou reprovado
if media >=7:
    print("Aprovado")   
else:   print("Reprovado kk burrão esse aluno")

print(f"A média das notas é: {media}")