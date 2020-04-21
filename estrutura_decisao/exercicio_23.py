numero = float(input("Digite um número: "));

if(numero == round(numero)):
    print("O número", round(numero), "é inteiro");
else:
    print("O número", numero, "é decimal",
          "\nO número", round(numero - 0.5), "arredondado para baixo",
          "\nO número", round(numero+0.5), "arredondado para cima");