valor = int(input("Digite uma valor positivo ou negativo: "));

if(valor > 0):
    print("O valor", valor, "é positivo");
elif(valor < 0):
    print("O valor", valor, "é negativo");
else:
    print("O valor", valor, "é igual a zero");