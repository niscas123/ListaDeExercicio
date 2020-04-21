salario = int(input("Digite o salário do seu colaborador: "));

if(salario <= 280):
    porcentagem = (20 / 100) * salario;
    resultado = salario + porcentagem;
    print(" -- Salário antes do reajuste: R$", salario,
          " \n-- Percentual de aumento aplicado:", 20,"%",
          " \n-- Valor do aumento: R$", porcentagem,
          " \n-- Novo salário: R$", resultado);
elif(salario > 280 and salario <= 700):
    porcentagem = (15 / 100) * salario;
    resultado = salario + porcentagem;
    print(" -- Salário antes do reajuste: R$", salario,
          " \n-- Percentual de aumento aplicado:", 15,"%",
          " \n-- Valor do aumento: R$", porcentagem,
          " \n-- Novo salário: R$", resultado);
elif(salario > 700 and salario <= 1500):
    porcentagem = (10 / 100) * salario;
    resultado = salario + porcentagem;
    print(" -- Salário antes do reajuste: R$", salario,
          " \n-- Percentual de aumento aplicado:", 10,"%",
          " \n-- Valor do aumento: R$", porcentagem,
          " \n-- Novo salário: R$", resultado);
elif(salario > 1500):
    porcentagem = (5 / 100) * salario;
    resultado = salario + porcentagem;
    print(" -- Salário antes do reajuste: R$", salario,
          " \n-- Percentual de aumento aplicado:", 5,"%",
          " \n-- Valor do aumento: R$", porcentagem,
          " \n-- Novo salário: R$", resultado);