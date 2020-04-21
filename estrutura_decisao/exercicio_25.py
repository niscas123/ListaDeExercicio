contador = 0;

resposta = str(input("Telefonou para a vítima? ")).lower();
if(resposta == "sim" or resposta =="s"):
    contador += 1;

resposta = str(input("Esteve no local do crime? ")).lower();
if(resposta == "sim" or resposta =="s"):
    contador += 1;

resposta = str(input("Mora perto da vítima? ")).lower();
if(resposta == "sim" or resposta =="s"):
    contador += 1;

resposta = str(input("Devia para a vítima? ")).lower();
if(resposta == "sim" or resposta =="s"):
    contador += 1;

resposta = str(input("Já trabalhou com a vítima? ")).lower();
if(resposta == "sim" or resposta =="s"):
    contador += 1;

if(contador == 2):
    print("Suspeit(a)");
elif(contador == 3 or contador == 4):
    print("Cúmplice");
elif(contador == 5):
    print("Assassino");
else:
    print("Inocente");



