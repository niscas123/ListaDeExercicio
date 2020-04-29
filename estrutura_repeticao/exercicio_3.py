# Nome com menos de 3 caracteres entra na funcao de repeticao
nome = str(input("Digite seu nome: "));
while(len(nome) < 3):
    nome = str(input("Digite seu nome: "));

# Idade menor que 0 ou maior que 150 entra na funcao de repeticao
idade = int(input("Digite sua idade: "));
while(idade < 0 or idade > 150):
    idade = int(input("Digite sua idade: "));

# Salario menor que 0 entra na funcao de repeticao
salario = float(input("Digite o seu salário: "));
while(salario < 0):
    salario = float(input("Digite o seu salário: "));

# Se a string de sexo for diferente de m ou f entra na funcao de repeticao
sexo = "";
while(sexo != "m" and sexo != "f"):
    sexo = str(input("Digite o seu sexo: "));
if (sexo == "m"):
    sexo = "Masculino";
elif (sexo == "f"):
    sexo = "Feminino";
else:
    print("\n ----- OPÇÃO INVÁLIDA! ----- \n");

# Se a string for diferente de s, c, v, ou d, entra na funcao de repeticao
estado_civil = "";
while(estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
    estado_civil = str(input("Digite o seu estado civil: ")).lower();
if(estado_civil == "s"):
    estado_civil = "Solteiro(a)";
elif(estado_civil == "c"):
    estado_civil = "Casado(a)";
elif(estado_civil == "v"):
    estado_civil = "Viúvo(a)";
elif(estado_civil == "d"):
    estado_civil = "Divorciado(a)";
else:
    print("\n ----- OPÇÃO INVÁLIDA! ----- \n");

print("\n ----- CADASTRO REALIZADO ----- "
      "\n ----- NOME:", nome,
      "\n ----- IDADE:", idade,
      "\n ----- SALÁRIO: R$%.2f" %salario,
      "\n ----- SEXO:", sexo,
      "\n ----- ESTADO CIVIL:", estado_civil);