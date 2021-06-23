a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
c=int(input("Digite o 3º número: "))

if (a < b < c):
	print("Os números foram digitados em ordem crescente!")

if (a < c < b) and (b > c > a):
	print("Os números não foram digitados em ordem crescente ou decrescente!")

if (b < a < c) and (c > a > b):
	print("Os números não foram digitados em ordem crescente ou decrescente!")

if (b < c < a) and (a > c > b):
	print("Os números não foram digitados em ordem crescente ou decrescente!") 

if (c < a < b) and (b > a > c):
	print("Os números não foram digitados em ordem crescente ou decrescente!")

if (c < b < a) and (c > b > a):
	print("Os números não foram digitados em ordem crescente ou decrescente!")

if (a > b > c):
	print("Os números foram digitados em ordem decrescente!")







