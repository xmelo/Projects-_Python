n1=float(input("Qual foi a nota do Trabalho de Laboratório?"))
n2=float(input("Qual foi a nota da avaliação semestral?"))
n3=float(input("Qual foi a nota do Exame Final do Aluno?"))

mepo=((n1*2) + (n2*3) + (n3*5)) / 10

if (mepo>=8 and mepo<=10):
	print("Conceito A")

elif (mepo>=7 and mepo<=7.9):
	print("Conceito B")

elif (mepo>=6 and mepo<=6.9):
	print("Conceito C")

elif (mepo>=5 and mepo<=5.9):
	print("Conceito D")

elif (mepo>=4 and mepo<=4.9):
	print("Conceito E")

