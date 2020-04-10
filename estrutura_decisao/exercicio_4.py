letra = str(input("Digite uma letra vogal ou consoante: ").lower());

if(letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra == "u"):
    print("A letra digitada", letra, "é vogal");
else:
    print("A letra digitada", letra, "é consoante");