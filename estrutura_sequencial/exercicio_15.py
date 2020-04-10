ganho_por_hora = float(input("Digite o valor de ganho por hora: "));
horas_trabalhadas = float(input("Digite as horas trabalhadas por mês: "));

salario_bruto = ganho_por_hora * horas_trabalhadas;
ir = (11 / 100.0 * salario_bruto);
inss = (8 / 100.0 * salario_bruto);
sindicato = (5 / 100.0 * salario_bruto);

imposto_total = ir + inss + sindicato;
salario_liquido = salario_bruto - imposto_total;
print("\n--| + Salário Bruto: R$ %2.f" %salario_bruto,
      "\nValor dos Impostos:"
      "\n--| - IR: R$ %2.f" %ir,
      "\n--| - INSS: R$ %2.f" %inss,
      "\n--| - Sindicato: R$ %2.f" %sindicato,
      "\n--| = Salário líquido: R$ %2.f" %salario_liquido);