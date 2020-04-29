numero = int(input("Digite um valor: "));
anterior = 1;
proximo = 1;
termo = 1;
if(numero == "1" or numero == "2"):
    print("1");
else:
    for f in range(0, numero):
        print(anterior);
        termo = proximo + anterior;
        anterior = proximo;
        proximo = termo;
        f += 1;
    #print(proximo);