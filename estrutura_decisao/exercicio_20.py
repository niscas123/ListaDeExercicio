nota_1 = float(input("1ª nota do aluno: "));
nota_2 = float(input("2ª nota do aluno: "));
nota_3 = float(input("3ª nota do aluno: "));

media = (nota_1 + nota_2 + nota_3) / 3;

if(media == 10):
    print("Aprovado com Distinção");
elif(media >= 7):
    print("Aprovado");
elif(media < 7):
    print("Reprovado");