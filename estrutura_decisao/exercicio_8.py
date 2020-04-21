#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_1 = float(input("Digite o preço do 1º produto: "));
produto_2 = float(input("Digite o preço do 2º produto: "));
produto_3 = float(input("Digite o preço do 3º produto: "));

menor = produto_1;
igual = produto_1;

#Verificando o menor valor do produto.
if(menor < produto_2 and produto_3):
    menor = produto_1;
    print("O 1º produto é o mais barato com o valor de {}".format(menor));
if(produto_2 < menor and produto_3):
    menor = produto_2;
    print("O 2º produto é o mais barato com o valor de {}".format(menor));
if(produto_3 < menor and produto_2):
    menor = produto_3;
    print("O 3º produto é o mais barato com o valor de {}".format(menor));

#Verificand se os produtos são dos preços iguais.
if(igual == produto_2 and igual and produto_2 < produto_3):
    print("O 1º produto e o 2º produto são os mais baratos com o valor de 1º produto: R$", produto_1, "e o 2º produto: R$",produto_2);
if(igual == produto_3 and igual and produto_3 < produto_2):
    print("O 1º produto e o 3º produto são os mais baratos com o valor de 1º produto: R$", produto_1, "e o 3º produto: R$", produto_3);
if(produto_2 == produto_3 and produto_2 and produto_3 < igual):
    print("O 2º produto e o 3º produto são os mais baratos com o valor de 2º produto: R$", produto_2, "e o 3º produto: R$", produto_3);