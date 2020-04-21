tipo = str(input("Tipo de combustível:"
                 "\nG - Gasolina"
                 "\nA - Alcool"
                 "\nDigite o tipo: "));
litros = float(input("Digite a quantidade de litros: "));

gasolina = 2.50;
custo_g = litros * gasolina;

alcool = 1.90;
custo_a = litros * alcool;

if(tipo == "G" or tipo == "gasolina"):
    if(litros <= 20):
        desconto = (custo_g / 100) * 4;
        print("O valor da gasolina com o desconto é de", custo_g - desconto);
    elif(litros > 20):
        desconto = (custo_g / 100) * 6;
        print("O valor da gasolina com o desconto é de", custo_g - desconto);

if(tipo == "A" or tipo == "alcool"):
    if(litros <= 20):
        desconto = (custo_a / 100) * 3;
        print("O valor do alcool com o desconto é de", custo_a - desconto);
    elif(litros > 20):
        desconto = (custo_a / 100) * 5;
        print("O valor do alcool com o desconto é de", custo_a - desconto);
else:
    print("Opção inválida");