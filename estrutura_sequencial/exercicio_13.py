genero = str(input("Digite o gênero que queira escolher, M para Masculino e F para Feminino: "));
altura = float(input("Digite a sua altura: "));

if(genero == "M" or genero == "masculino"):
    peso_m = (72.7 * altura) - 58;
    print("Seu peso ideal é %.2f" %peso_m);
elif(genero == "F" or genero == "feminino"):
    peso_f = (62.1 * altura) - 44.7;
    print("Seu pedo ideal é %.2f" %peso_f);
else:
    print("Opção inválida");