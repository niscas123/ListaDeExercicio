num_1 = int(input("Digite o primeiro número: "));
num_2 = int(input("Digite o segundo número: "));
num_3 = int(input("Digite o terceiro número: "));

if(num_1 > num_2 and num_1 > num_3):
    print("O primeiro número", num_1, "é maior que o segundo número", num_2, "e o terceiro número", num_3);
elif(num_2 > num_1 and num_2 > num_3):
    print("O segundo número", num_2, "é maior que o primeiro número", num_1, "e o terceiro número", num_3);
elif(num_3 > num_1 and num_3 > num_2):
    print("O terceiro número", num_3, "é maior que o primeiro número", num_1, "e o segundo número", num_2);