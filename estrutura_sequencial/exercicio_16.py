metros = float(input("Digite a quantidade de m² a serem pintados: "));
litros = metros/3;

preco_litro = 80;
capacidade_litro = 18;

latas = litros / capacidade_litro;
preco_total = latas * preco_litro;

print("Será usado %2.f" %latas, "latas de tinta",
      "\nO preço total é de: R$%2.f" %preco_total);

