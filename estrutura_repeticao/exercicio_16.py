numero = int(input("Digite um valor que o resultado seja < 500 na fórmula Fibonacci: "));

anterior = 0;
proximo = 1;
termo = 1;

if(numero == "1" or numero == "2"):
    print("1");
else:
    for f in range(0, numero):
        #print(anterior);
        termo = proximo + anterior;
        anterior = proximo;
        proximo = termo;
        f += 1;
        if (anterior <= 500):
            print(anterior);
        else:
            print("Resultado referente a > 500 não permitido");
            break;
