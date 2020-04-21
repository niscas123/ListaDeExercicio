num_1 = int(input("Digite o primeiro número: "));
num_2 = int(input("Digite o segundo número: "));
num_3 = int(input("Digite o terceiro número: "));

maior = num_1;
menor = num_1;
igual = num_1

#Verificando o maior número
if(num_2 > num_1 and num_3):
    maior = num_2;
if(num_3 > num_1 and num_2):
    maior = num_3;

#Verificando o menor número
if(num_2 < num_1 and num_3):
    menor = num_2;
if(num_3 < num_1 and num_2):
    menor = num_3;

print("O maior número é {}".format(maior), "\nO menor número é {}".format(menor));

