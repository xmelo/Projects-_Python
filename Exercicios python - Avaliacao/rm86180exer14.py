r1=float(input("Digite a medida do primeiro lado do triangulo:"))
r2=float(input("Digite a medida do segundo lado do triangulo:"))
r3=float(input("Digite a medida do terceiro lado do triangulo:"))

if r1 == r2 == r3:
	print ("Triangulo equilátero!")
if r1 != r2 != r3 != r1:
	print ("Triangulo escaleno!")
elif (r1 == r2 != r3):
	print ("Triangulo Isósceles!")

