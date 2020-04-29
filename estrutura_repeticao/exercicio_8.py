soma = 0;
media = 0;

#O laco de repeticao pede 5 números para ser digitado
for i in range(1, 6):
    numero = int(input("Digite o {}ª número: ".format(i)));
    # E feito a soma de todos o numeros para posteriormente
    # realizar a media dessa soma pegando a quantidade de numeros digitados
    soma += numero;
    media = soma / i;

print("A soma de todos os números digitados é: %.0f" %soma,
      "\nE a média dessa soma é: %.0f" %media);