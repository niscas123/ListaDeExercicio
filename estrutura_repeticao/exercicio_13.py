base = float(input("Base ^ Expoente"
                   "\nBase: "));
expoente = float(input("Expoente: "));

potencia = 1;
contador = 1;
while(contador <= expoente):
    potencia = potencia * base;
    contador += 1;
print(base, "^", expoente, "=", potencia);