nom=str(input("Informe o nome do aluno: "))
print(nom)
not1=int(input("Informe a primeira nota do aluno: "))
not2=int(input("Informe a segunda nota do aluno: "))
not3=int(input("Informe a terceira nota do aluno: "))
fal=int(input("Informe o número de faltas do aluno:"))
print(fal)

med=(not1 + not2 + not3) / 3

#fal=80*0,25=20

if med >= 7:
	print (f"O aluno ", nom, " está aprovado.")

elif fal > 20:
	print (f"O aluno ", nom, " está reprovado. Por excesso de faltas")

elif med <7:
	print (f"O aluno ", nom, " está reprovado.")
