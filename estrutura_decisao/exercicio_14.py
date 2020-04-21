nota_1 = float(input("Digite a 1ª nota parcial: "));
nota_2 = float(input("Digite a 2ª nota parcial: "));

media = (nota_1 + nota_2) / 2;

if(media >= 9 or media == 10.0):
    print("A = EXCELENTE!");
elif(media >= 7.5 and media < 9.0):
    print("B = APROVADO!");
elif(media >= 6.0 and media < 7.5):
    print("C = APROVADO!");
elif(media >= 4.0 and media < 6.0):
    print("D = REPROVADO!");
elif(media >= 0.0 and media < 4.0):
    print("E = REPROVADO!");
else:
    print("Valor inválido.");