horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "));
ganho_horas = int(input("Digite o ganho por horas: "));

salario_bruto = ganho_horas * horas_trabalhadas;

if(salario_bruto <= 900):
    ir = (salario_bruto / 100) * 0;
    inss = (salario_bruto / 100) * 10;
    fgts = (salario_bruto / 100) * 11;
    desconto = ir + inss;
    print("--- O salário bruto é: R$", salario_bruto,
          "\n--- (-)IR (5%): R$", ir,
          "\n--- (-)INSS (10%): R$", inss,
          "\n--- FGTS (11%): R$", fgts,
          "\n--- Total de desconto: R$", desconto,
          "\n--- Salário líquido: R$", salario_bruto - desconto);
elif(salario_bruto > 900 and salario_bruto <= 1500):
    ir = (salario_bruto / 100) * 5;
    inss = (salario_bruto / 100) * 10;
    fgts = (salario_bruto / 100) * 11;
    desconto = ir + inss;
    print("--- O salário bruto é: R$", salario_bruto,
          "\n--- (-)IR (5%): R$", ir,
          "\n--- (-)INSS (10%): R$", inss,
          "\n--- FGTS (11%): R$", fgts,
          "\n--- Total de desconto: R$", desconto,
          "\n--- Salário líquido: R$", salario_bruto - desconto);
elif(salario_bruto > 1500 and salario_bruto <= 2500):
    ir = (salario_bruto / 100) * 10;
    inss = (salario_bruto / 100) * 10;
    fgts = (salario_bruto / 100) * 11;
    desconto = ir + inss;
    print("--- O salário bruto é: R$", salario_bruto,
          "\n--- (-)IR (10%): R$", ir,
          "\n--- (-)INSS (10%): R$", inss,
          "\n--- FGTS (11%): R$", fgts,
          "\n--- Total de desconto: R$", desconto,
          "\n--- Salário líquido: R$", salario_bruto - desconto);
elif(salario_bruto > 2500):
    ir = (salario_bruto / 100) * 20;
    inss = (salario_bruto / 100) * 10;
    fgts = (salario_bruto / 100) * 11;
    desconto = ir + inss;
    print("--- O salário bruto é: R$", salario_bruto,
          "\n--- (-)IR (20%): R$", ir,
          "\n--- (-)INSS (10%): R$", inss,
          "\n--- FGTS (11%): R$", fgts,
          "\n--- Total de desconto: R$", desconto,
          "\n--- Salário líquido: R$", salario_bruto - desconto);
else:
    print("Opção inválida");
