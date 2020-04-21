opcao = str(input("Tipos de alimento"
                  "\nmorango - Morango até 5kg R$2,50 e acima de 5kg R$2,20"
                  "\nmaca - Maca até 5kg R$1.80 e acima de kg R$1.50"
                  "\nDigite aqui a opção que será escolhida: "));

if(opcao == "morango" or opcao == "mo"):
    kg = float(input("Digite a quantidade em Kg: "));
    if(kg <= 5):
        custo = kg * 2.50;
        print("O preço é de", custo, "do morango abaixo de 5kg");
    elif(kg > 5 or kg <= 8):
        custo = kg * 2.20;
        print("O preço é de", custo, "do morango acima de 5kg");
        if(kg > 8 or custo > 25):
            desconto = (custo / 100) * 10;
            print("O preço é de", custo, "do morango acima de 8kg ou valor acima de R$25,00");

if(opcao == "maca" or opcao == "ma"):
    kg = float(input("Digite a quantidade em Kg: "));
    if(kg <= 5):
        custo = kg * 1.80;
        print("O preço é de", custo, "da maçã abaixo de 5kg");
    elif(kg > 5 or kg <= 8):
        custo = kg * 1.50;
        print("O preço é de", custo, "da maçã acima de 5kg");
        if(kg > 8 or custo > 25):
            desconto = (custo / 100) * 10;
            print("O preço do", custo, "de maçã acima de 8kg ou valor acima de R$25,00");
else:
    print("Opção inválida!");



