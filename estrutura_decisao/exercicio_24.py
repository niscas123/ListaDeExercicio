numero_1 = float(input("Digite o 1ª número: "));
numero_2 = float(input("Digite o 2ª número: "));
opcao = str(input(" --- Escolha a opção que deseja --- "
                  "\n --- + - Soma"
                  "\n --- - - Subtração"
                  "\n --- / - Divisão"
                  "\n --- * - Multiplicação"
                  "\nDigite a sua opção: "))
if(opcao == "+"):
    resultado = numero_1 + numero_2;
elif(opcao == "-"):
    resultado = numero_1 - numero_2;
elif(opcao == "/"):
    resultado = numero_1 / numero_2;
elif(opcao == "*"):
    resultado = numero_1 * numero_2;
else:
    print("A opção está inválida");

print("Resultado =", resultado);

if(resultado % 2 != 0):
    print("O resultado:", resultado, "é ímpar");
else:
    print("O resultado:", resultado, "é par");

if(resultado >= 0):
    print("O resultado:", resultado, "é positivo");
else:
    print("O resultado:", resultado, "é negativo");

if(resultado == round(resultado)):
    print("O resultado:", round(resultado), "é inteiro");
else:
    print("O resultado:", round(resultado - 0.5), "é decimal arredondado para baixo");
    print("O resultado:", round(resultado + 0.5), "é decimal arredondado para cima");

