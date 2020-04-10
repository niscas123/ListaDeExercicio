peso_do_peixe = float(input("Digite o peso do peixe em Kg: "));

if(peso_do_peixe > 50):
    excesso = peso_do_peixe - 50;
    multa = excesso * 4;
    print("Você excedeu o peso de %2.f" %excesso,
          "Kg do número permitido de peixes \nO valor da multa é de R$ %2.f" %multa);
else:
    print("Você não excedeu o limite de peixes pescados.")