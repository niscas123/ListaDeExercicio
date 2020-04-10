nota_1 = float(input("Digite a primeira nota parcial do aluno: "));
nota_2 = float(input("Digite a segunda nota parcial do aluno: "));

media = (nota_1 + nota_2) / 2;

if(media == 10):
    print("O aluno foi Aprovado com Distinção");
elif(media >= 7):
    print("O aluno foi Aprovado");
elif(media < 7):
    print("O aluno foi Reprovado");
else:
    print("A média do aluno está incorreta");