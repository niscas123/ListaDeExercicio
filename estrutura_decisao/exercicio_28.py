cartao = str(input("Você tem o cartão Tabajara? ")).lower();

kg = float(input("Digite o peso requerido da carne em kg: "));

if(cartao == "sim"):
    tipo = str(input("fl - Filé duplo"
               "\nal - Alcatra"
               "\npi - Picanha:"
               "\nDigite a opção de carne: "));
    if(tipo == "fl"):
        if(kg <= 5):
            custo = kg * 4.90;
            desconto = (custo / 100) * 5;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f" %desconto,
                  "\nValor a Pagar = R$%.2f" %(custo - desconto));
        elif(kg > 5):
            custo = kg * 5.80;
            desconto = (custo / 100) * 5;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f" %desconto,
                  "\nValor a Pagar = R$%.2f" %(custo - desconto));
    elif(tipo == "al"):
        if(kg <= 5):
            custo = kg * 5.90;
            desconto = (custo / 100) * 5;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f" %desconto,
                  "\nValor a Pagar = R$%.2f" %(custo - desconto));
        elif(kg > 5):
            custo = kg * 6.80;
            desconto = (custo / 100) * 5;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f" %desconto,
                  "\nValor a Pagar = R$%.2f" %(custo - desconto));
    elif(tipo == "pi"):
        if(kg <= 5):
            custo = kg * 6.90;
            desconto = (custo / 100) * 5;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f" %desconto,
                  "\nValor a Pagar = R$%.2f" %(custo - desconto));
        elif(kg > 5):
            custo = kg * 7.80;
            desconto = (custo / 100) * 55;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f" %desconto,
                  "\nValor a Pagar = R$%.2f" %(custo - desconto));
    else:
        print("Opção Inválida!");
elif(cartao == "nao"):
    tipo = str(input("fl - Filé duplo"
               "\nal - Alcatra"
               "\npi - Picanha:"
               "Digite a opção de carne: "));
    if(tipo == "fl"):
        if(kg <= 5):
            custo = kg * 4.90;
            print(" --- MERCADO TABAJARA --- "
                  "\nProduto comprado = Filé Duplo"
                  "\nQuantidade = %.2fkg" %kg,
                  "\nPreço Total = R$%.2f" %custo,
                  "\nTipo de Pagamento = Cartão"
                  "\nValor Descontado = R$%.2f",
                  "\nValor a Pagar = R$%.2f" %custo);
        elif(kg > 5):
            if (kg <= 5):
                custo = kg * 5.80;
                print(" --- MERCADO TABAJARA --- "
                      "\nProduto comprado = Filé Duplo"
                      "\nQuantidade = %.2fkg" % kg,
                      "\nPreço Total = R$%.2f" % custo,
                      "\nTipo de Pagamento = Cartão"
                      "\nValor Descontado = R$%.2f",
                      "\nValor a Pagar = R$%.2f" % custo);
        if(tipo == "al"):
            if (kg <= 5):
                custo = kg * 5.90;
                print(" --- MERCADO TABAJARA --- "
                      "\nProduto comprado = Filé Duplo"
                      "\nQuantidade = %.2fkg" % kg,
                      "\nPreço Total = R$%.2f" % custo,
                      "\nTipo de Pagamento = Cartão"
                      "\nValor Descontado = R$%.2f",
                      "\nValor a Pagar = R$%.2f" % custo);
            elif (kg > 5):
                if (kg <= 5):
                    custo = kg * 6.80;
                    print(" --- MERCADO TABAJARA --- "
                          "\nProduto comprado = Filé Duplo"
                          "\nQuantidade = %.2fkg" % kg,
                          "\nPreço Total = R$%.2f" % custo,
                          "\nTipo de Pagamento = Cartão"
                          "\nValor Descontado = R$%.2f",
                          "\nValor a Pagar = R$%.2f" % custo);
        if(tipo == "pi"):
            if (kg <= 5):
                custo = kg * 6.90;
                print(" --- MERCADO TABAJARA --- "
                      "\nProduto comprado = Filé Duplo"
                      "\nQuantidade = %.2fkg" % kg,
                      "\nPreço Total = R$%.2f" % custo,
                      "\nTipo de Pagamento = Cartão"
                      "\nValor Descontado = R$%.2f",
                      "\nValor a Pagar = R$%.2f" % custo);
            elif (kg > 5):
                if (kg <= 5):
                    custo = kg * 7.80;
                    print(" --- MERCADO TABAJARA --- "
                          "\nProduto comprado = Filé Duplo"
                          "\nQuantidade = %.2fkg" % kg,
                          "\nPreço Total = R$%.2f" % custo,
                          "\nTipo de Pagamento = Cartão"
                          "\nValor Descontado = R$%.2f",
                          "\nValor a Pagar = R$%.2f" % custo);
else:
    print("Opção inválida!");