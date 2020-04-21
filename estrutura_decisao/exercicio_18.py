dia = int(input("Digite o dia: "));
mes = int(input("Digite o mês: "));
ano = int(input("Digite o ano: "));

valido = False;

#Meses com até 31 dias.
if(mes < 1 or mes > 12 or dia < 1 or dia > 31 or ano < 1):
    print("A data de", dia, "/", mes, "/", ano, " é inválido");
else:
    # Meses com até 31 dias.
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if(dia <= 31):
            valido = True;
        #Meses com até 30 dias.
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia <= 30):
            valido = True;
    elif(mes == 2):
        # Ano bissexto.
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if (mes == 2 and dia <= 29):
                valido = True;
            elif(dia <= 28):
                valido = True;
    if(valido == True):
        valido = True;
        print("A data do ano de", dia, "/", mes, "/", ano, "é válido");
    else:
        print("A data de", dia, "/", mes, "/", ano, "é inválido");