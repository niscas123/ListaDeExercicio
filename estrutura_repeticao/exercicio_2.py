usuario = "";
senha = "";
erro_cadastro = "\n ---- DIGITE NOVAMENTE SUA SENHA COM CARACTERES DIFERENTES DO USUÁRIO ---- \n";

while(senha == usuario):
    usuario = str(input("Digite seu usuário para inscrição: "));
    senha = str(input("Digite sua senha pra inscrição: "));
    if(usuario == senha):
        print(erro_cadastro);
else:
    print("\n ---- SEU USUÁRIO E SENHA FORAM CONFIRMADOS ---- ");