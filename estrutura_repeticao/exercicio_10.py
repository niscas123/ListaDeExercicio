numero_1 = int(input("Digite o 1ª número: "));
numero_2 = int(input("Digite o 2ª número: "));

while(numero_1 != numero_2):
    numero_1 = int(input("Digite o 1ª número: "));
    numero_2 = int(input("Digite o 2ª número: "));
else:
    for i in range(numero_1, numero_2, 1):
        print(i);