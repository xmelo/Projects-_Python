salario = float(input('Qual o salario do funcionario? R$'))
novo = salario + (salario * 20 /100)
print('O funcionario que ganhava R${:2f}, com 20% de aumento passa a ganhar R${:2f}'. format(salario,novo))