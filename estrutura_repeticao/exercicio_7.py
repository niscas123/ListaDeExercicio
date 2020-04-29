maior = 0;

for i in range(5):
    i += 1;
    numero = int(input("Digite o {}ª número: ".format(i)));
    if(numero > maior):
        maior = numero;
print("O maior número digitado é", maior);