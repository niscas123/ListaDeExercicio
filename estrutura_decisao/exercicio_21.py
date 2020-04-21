valor = float(input("Digite o valor do saque requerido: "));

if(valor < 10):
    print("O valor do saque digitado está indisponível.");
else:
    cem = valor / 100;
    valor = valor % 100;

    cinquenta = valor / 50;
    valor = valor % 50;

    dez = valor / 10;
    valor = valor % 10;

    cinco = valor / 5;
    valor = valor % 5;

    um = valor;

    print("Notas R$100,00 =", int(cem),
          "\nNotas R$50,00 =", int(cinquenta),
          "\nNotas R$10,00 =", int(dez),
          "\nNotas R$5,00 =", int(cinco),
          "\nNotas R$1,00 =", int(um));