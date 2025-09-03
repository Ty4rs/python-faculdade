


def texto(conteudo):
    print("╔══" + (len(conteudo) * "═") + "══╗")
    print("║  " + conteudo + "  ║")
    print("╚══" + (len(conteudo) * "═") + "══╝")
    

def pergunta(pergunta, *conteudo):
    valor = 0
    if len(pergunta) > len(max(conteudo, key=len)):

        valor = len(pergunta)
        print("╔══" + (valor * "═") + "══╗")
        print("║  " + pergunta + "  ║")
    else:
        valor = len(max(conteudo, key=len))
        print("╔══" + (valor * "═") + "══╗")
        print("║  " + (int((len(max(conteudo, key=len)) - len(pergunta)) /2) * " ")  +   pergunta  + (int((len(max(conteudo, key=len)) - len(pergunta)) /2) * " ") + "  ║")
    for i in range(len(conteudo)):
        if (i == len(conteudo) - 1):
            print("╠══" + (valor * "═") + "══╣")
            print("║  " + (conteudo[i]) + ((valor - len(conteudo[i])) * " ") + "  ║")
            print("╚══" + (valor * "═") + "══╝")
        else:
            print("╠══" + (valor * "═") + "══╣")
            print("║  " + (conteudo[i]) + ((valor - len(conteudo[i])) * " ") + "  ║")
            
        

    
        
texto("oi")        
pergunta("oi", "oii", "aaaopaaaaaaaaaaaaaaaaaaaaaaa", "asdasf")