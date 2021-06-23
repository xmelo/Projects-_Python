a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
c=int(input("Digite o 3º número: "))

if (a > b > c):
	print(f"Os números na forma decrescente são:{a,b,c}")

if (a > c > b):
	print(f"Os números na forma decrescente são:{a,c,b}")

if (b > a > c):
	print(f"Os números na forma decrescente são:{b,a,c}")

if (b > c > a):
	print(f"Os números na forma decrescente são:{b,c,a}") 

if (c > a > b):
	print(f"Os números na forma decrescente são:{c,a,b}")

if (c > b > a):
	print (f"Os números na forma decrescente são:{c,b,a}")


