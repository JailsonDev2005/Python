
def menu():
    conteudo = "Escalha uma opçâo"
    conteudo += "\n1 - Criar usuário"
    conteudo += "\n2 - Deletar usuário"
    conteudo += "\n3 - Atualizar usuário"
    conteudo += "\n4 - Lista usuário"

    
    print(conteudo)

    opcao = int(input("Digite o número da opçâo: "))
    return opcao


def check_option(option):
    if option < 1 or option > 4:
        return True


def main():
    escolha = menu()
    while check_option(escolha):
        
        


    print(f"Você escolheu: {escolha}")




if __name__ == "__main__":
    main()