nota = float(input("Digite uma nota entre 0 a 10: "));

while(nota < 0 or nota > 10):
    print("\n --- Digite outro número conforme o enunciado. --- \n");
    nota = float(input("Digite uma nota entre 0 a 10: "));
else:
    print("Nota: %.0f" %nota);