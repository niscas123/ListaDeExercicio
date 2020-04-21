numero = int(input("Digite um número positivo: "));

#Transformando em unidade
unidade = numero % 10;

#Excluindo a unidade do numero
numero = (numero - unidade) / 10;

#Transformando em dezena
dezena = numero % 10;

#Excluindo a dezena do numero, para virar a centena
numero = (numero - dezena) / 10;
centena = numero;

print(int(centena), "centena(s)", int(dezena), "dezena(s) e", int(unidade), "unidade(s)");