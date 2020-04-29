soma = 0;

for i in range(1, 3):
    numero = int(input("Digite o {}ª número: ".format(i)));
    soma += numero;
print("A soma dos números é:", soma);