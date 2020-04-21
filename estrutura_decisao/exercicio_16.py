import math

a = float(input("Digite os termos da equação em 2 grau, como a, b, c da fórmula: ax² + bx + c"
                "\nDigite o termo a da equação: "));
if(a == 0):
    print("Não é equação do 2 grau");
else:
    b = float(input("Digite o termo b da equação: "));
    c = float(input("Digite o termo c da equação: "));

    delta = (b ** 2) - (4 * a * c);

    if(delta < 0):
        print("delta = ", delta, "a equação não possui raízes reais");
    elif(delta == 0):
        print("Delta = ", delta, "a equação possui uma raíz");
        raiz = (-b) + (math.sqrt(delta)) / (2 * a);
        print("Delta = 0, raíz", raiz);
    else:
        raiz_x1 = (-b) + (math.sqrt(delta));
        x1 = raiz_x1 / (2 * a);
        raiz_x2 = (-b) - (math.sqrt(delta));
        x2 = raiz_x2 / (2 * a);
        print("A equação possui duas raízes:"
              "\nRaíz x1: ", x1,
              "\nRaíz x2: ", x2);
