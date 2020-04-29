a = 80000;
b = 200000;
ano = 0;
cresc_a = 3 / 100;
cresc_b = 1.5 / 100;

while(a <= b):
    a = (a + a) * cresc_a;
    b = (b + b) * cresc_b;
    ano += 1;

print("A população A ultrapassou a população B após %d anos" %ano,
      "\nPopulação A: %.0f mil" %a,
      "\nPopulação B: %.0f mil" %b);


