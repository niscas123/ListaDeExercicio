entrada = str(input("Digite o produto que queira requisitar L para litro, G para galão e LG para galão e litro: "));
metros = float(input("Digite a quantidade em m² a serem pintados: "));

litros = float(metros / 6);
preco_litro = 80;

capacidade_litro = float(litros / 18);

litros_galao = float(metros / 3.6);
preco_galao = 25;

if(entrada == "L"):
    latas = litros / capacidade_litro;
    preco_litro = latas * preco_litro;
    print("O preço do galão ficará por: R$%.2f" % preco_litro);

elif(entrada == "G"):
    galao = litros_galao / capacidade_litro;
    preco_galao = galao * litros_galao;
    print("O preço do galão ficará por: R$%.2f" %preco_galao);

elif(entrada == "LG"):
    galao_latas = (litros / capacidade_litro) + (litros_galao / capacidade_litro);
    preco_galao_latas = galao_latas + (litros * litros_galao);
    desconto = (preco_galao_latas * 10) / 100;
    print("A lata com o galão ficaram por: R$%.2f" %preco_galao_latas,
          "\nCom o desconto de 10 porcento fica por R$%.2f" %(preco_galao_latas - desconto));
else:
    print("Opçção Inválida!");