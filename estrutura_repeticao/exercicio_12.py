tabuada = int(input("Tabuada do número: "));

for i in range(10):
    resultado = tabuada * (i + 1);
    print("%d X %d = %d" %(tabuada, i + 1, resultado));