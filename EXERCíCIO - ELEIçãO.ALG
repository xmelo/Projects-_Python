Algoritmo "Exercício - Eleição"
// Disciplina  :  [Linguagem e Lógica de Programação] 
// Professor   : Fernanda
// Descrição   : Exercício -  Eleição
// Autor(a)    : Artaxerxes Antonio de Melo
// Data atual  : 07/03/2020
Var
// Seção de Declarações das variáveis 
nome: caracter
n1,n2,n3,n4,n5: real
soma: real
valor: inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval ("Digite a quantidade de votos do candidato A:")
leia(n1)
escreval ("Digite a quantidade de votos do candidato B:")
leia(n2)
escreval ("Digite a quantidade de votos do candidato C:")
leia(n3)
escreval ("Digite a quantidade de votos Brancos:")
leia(n4)
escreval ("Digite a quantidade de votos Nulos:")
leia(n5)
escreval ("Quantidade total de votos (eleitores):")
leia soma <-- (n1+n2+n3+n4+n5)
escreval ("Porcentagem de votos do candidato A:",
leia valor  <-- (soma * n1\100 "%")
escreval ("Porcentagem de votos do candidato B:",
leia valor  <-- (soma * n2\100 "%")
escreval ("Porcentagem de votos do candidato C:",
leia valor  <-- (soma * n3\100 "%")
escreval ("Pocentagem de votos Brancos:",
leia valor <-- (soma * n4\100 "%")
escreval ("Porcentagem de votos Nulos",
leia valor <-- (soma * n5\100 "%")




Fimalgoritmo