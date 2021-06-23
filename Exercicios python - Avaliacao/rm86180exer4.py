a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
c=int(input("Digite o 3º número: "))

if (a < b < c):
	print(f"Os números na forma crescente são:{a,b,c}")

if (a < c < b):
	print(f"Os números na forma crescente são:{a,c,b}")

if (b < a < c):
	print(f"Os números na forma crescente são:{b,a,c}")

if (b < c < a):
	print(f"Os números na forma crescente são:{b,c,a}") 

if (c < a < b):
	print(f"Os números na forma crescente são:{c,a,b}")

if (c < b < a):
	print (f"Os números na forma crescente são:{c,b,a}")

if (a == b or a == c or b == c):
	print ("Os três números digitados são iguais!")