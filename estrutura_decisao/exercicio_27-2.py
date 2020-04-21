print(" ---- SEJA BEM VINDO AO FEIRA LIVRE ---- "
      "\n ------------- PREÇO DAS FRUTAS ------------- " 
      "\n ---- PREÇO POR KG  = ATÉ 5KG | ACIMA 5KG"
      "\n ---- MORANGO       = R$ 2,50 | R$ 1,80"
      "\n ---- MAÇÃ          = R$ 2,20 | R$ 1,50");

tipo_fruta = str(input("\nmorango para MORANGO"
                       "\nmaca para MAÇÃ"
                       "\nESCOLHA O TIPO DA FRUTA: ")).lower();

peso_fruta = float(input("QUANTOS KG DE FRUTAS O CLIENTE VAI QUERER? "));

#Classifica as frutas por peso e o preco dessas
if(peso_fruta >= 0 or peso_fruta <= 5):
    preco_morango = 2.50;
    preco_maca = 1.80;
elif(peso_fruta > 5 or peso_fruta <= 8):
    preco_morango = 2.20;
    preco_maca = 1.50;

#Escolhe o tipo de fruta que será comprada
if(tipo_fruta == "morango"):
    preco_bruto = peso_fruta * preco_morango;
    tipo = "Morango";
elif(tipo_fruta == "maca"):
    preco_bruto = peso_fruta * preco_maca;
    tipo = "Maçã";
else:
    print("Fruta digitada inexistente");

#Verifica se possui desconto apartir do peso ou do valor da fruta
if(peso_fruta > 8 or preco_bruto > 25):
    desconto = (preco_bruto / 100) * 10;
    preco_final = preco_bruto - desconto;
else:
    preco_final = preco_bruto;

#Fatura
print("\n -------- NOTA FISCAL --------"
      "\n ----- Tipo da Fruta =", tipo,
      "\n ----- Peso = R$ %.2f" %peso_fruta,
      "\n ----- Preço = R$ %.2f" %preco_bruto);

if(preco_final != preco_bruto):
    print(" ----- Desconto =", desconto,
          "\n ----- Preço Final = R$ %.2f" %preco_final);
else:
    print(" ----- Desconto = Não"
          "\n ----- Preço Final = R$ %.2f" %preco_final);