num1=int(input("Digite um número:"))

x= (num1 >=0) and (num1 <=30)
y= (num1 >=40) and (num1<=79)
z= (num1 > 30) and (num1 <40)
k= (num1>79)

if (x):
	print ("O número está compreendido entre 0 e 30!")

elif (y):
	print ("O número está compreendido entre 40 e 79!")

elif (z):
	print ("O número está fora dos limites estabelecidos!")

elif (k):
	print ("O número está fora dos limites estabelecidos!")
