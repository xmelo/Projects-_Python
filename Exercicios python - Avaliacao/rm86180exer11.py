num1=int(input("Digite um numero inteiro:"))
num2=int(input("Digite outro número inteiro:"))

x=num1>num2
y=num2>num1

if (x):
	print(f"O maior número é {num1}")

elif (y):
	print(f"O maior número é {num2}!")