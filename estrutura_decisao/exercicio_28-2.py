print(" ---- SEJA BEM VINDO AO MERCADO TABAJARA ---- "
      "\n ------------- PREÇO DAS CARNES ------------- " 
      "\n ---- PREÇO POR KG     = ATÉ 5KG | ACIMA 5KG"
      "\n ---- FILÉ DUPLO       = R$ 4,90 | R$ 5,80"
      "\n ---- ALCATRA          = R$ 5,90 | R$ 6,80"
      "\n ---- PICANHA          = R$ 6,90 | R$ 7,80");

#O comprador escolhe o tipo de carne
tipo_carne = str(input("\nF para FILÉ DUPLO"
                       "\nA para ALCATRA"
                       "\nP para PICANHA"
                       "\nESCOLHA O TIPO DA CARNE: ")).lower();

#O comprador escolhe o peso da carne
peso_carne = float(input("\nQUANTOS KG DE CARNE O CLIENTE DESEJA COMPRAR? "));

#Classifica as carnes pelo preco
if(peso_carne <= 5):
    preco_file = 4.90;
    preco_alcatra = 5.90;
    preco_picanha = 6.90;
else:
    preco_file = 5.80;
    preco_alcatra = 6.80;
    preco_picanha = 7.80;

#Definindo o preco da carne
if(tipo_carne == "f"):
    preco = peso_carne * preco_file;
    tipo = "Filé Duplo";
elif(tipo_carne == "a"):
    preco = peso_carne * preco_alcatra;
    tipo = "Alcatra";
elif(tipo_carne == "p"):
    preco = peso_carne * preco_picanha;
    tipo = "Picanha";
else:
    print("Tipo de carne inexistente");

cliente_tabajara = str(input("\nSim - sim"
                             "\nNão - nao"
                             "\nVocê é cliente Tabajara? ")).lower();
desconto = (preco / 100) * 5;

if(cliente_tabajara == "s" or cliente_tabajara == "sim"):
    preco_final = preco - desconto;
else:
    preco_final = preco;

#Fatura
print("\n -------- NOTA FISCAL --------"
      "\n ----- Tipo de Carne =", tipo,
      "\n ----- Peso = R$ %.2f" %peso_carne,
      "\n ----- Preço = R$ %.2f" %preco);
if(preco_final != preco):
    print(" ----- Desconto = R$ %.2f" %desconto,
          "\n ----- Preço Final = R$ %.2f" %preco_final);
else:
    print(" ----- Desconto = Não"
          "\n ----- Preço Final = R$ %.2f" %preco_final);