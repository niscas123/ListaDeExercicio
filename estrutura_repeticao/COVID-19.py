total_habitantes = 209.500000;
total_casos = 59.324;
mortes = 4.057;
recuperados = 29.160;

mortes_casos = (100 * mortes) / total_casos;
recuperados_casos = (100 * recuperados) / total_casos;
casos_habitantes = (100 * mortes) / total_habitantes;

print("Mortes por casos confirmados no Brasil por COVID-19: %.2f" %mortes_casos,
      "\nRecuperados por casos confirmados no Brasil por COVID-19: %.2f" %recuperados_casos,
      "\nCasos de COVID-19 por habitantes no Brasil: %.2f" %(casos_habitantes / total_casos));

# 100 x total_habitantes (209,500000)
# X   x mortes (4057)
# 100 x 4057 = 405,700 / total_habitantes