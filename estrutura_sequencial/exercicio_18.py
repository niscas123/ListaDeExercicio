tamanho_arquivo = float(input("Tamanho do arquivo em MB: "));
velocidade = float(input("Velocidade da internet em MB: "));

baixado = (tamanho_arquivo / velocidade) * 60;

print("O download será finalizado em %.0f minutos" %baixado);