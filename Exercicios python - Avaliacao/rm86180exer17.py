prod=float(input("Digite o valor da compra:"))

val=(prod < 20)

valr=(prod > 20)

x=(prod * 0.45 + prod)
y=(prod * 0.30 + prod)

if(val):
	print("O valor do produto será com margem de lucro de 45%, portanto o produto custará:" ,x, "R$")

elif(valr):
	print(f"O valor do produto será com margem de lucro de 30%, portanto o produto custará:" ,y, "R$")