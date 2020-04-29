popA = float(input("Digite a população da cidade A: "));
popB = float(input("Digite a população da cidade B: "));
ano = 0;
taxa_crescA = float(input("Digite a taxa de crescimento da população A: "));
taxa_crescB = float(input("Digite a taxa de crescimento da população B: "));

while(popA <= popB):
    popA = ((popA + popA) * taxa_crescA) / 100;
    popB = ((popB + popB) * taxa_crescB) / 100;
    ano = ano + 1;

print("Levará", ano, "anos para a população da cidade A ser maior que a cidade B",
      "\nPopulação A = %.0f" %popA, "mil habitantes"
      "\nPopulação B = %.0f" %popB, "mil habitantes");