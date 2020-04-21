lado_1 = float(input("Digite o valor do 1ª lado do triângulo: "));
lado_2 = float(input("Digite o valor do 2ª lado do triângulo: "));
lado_3 = float(input("Digite o valor do 3ª lado do triângulo: "));

if(lado_1 + lado_2 < lado_3 or lado_1 + lado_3 < lado_2 or lado_2 + lado_3 < lado_1):
    print("Não é um triângulo");
elif(lado_1 == lado_2 and lado_1 == lado_3):
    print("Equilátero");
elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
    print("Isósceles");
else:
    print("Escaleno");