from rich import print
from rich.table import Table
from rich.panel import Panel

Dados = []



def criar_cadastro(nome, idade, sexo, numero):
    cadastro = {"nome":nome, "idade":idade, "sexo":sexo, "numero":numero}
    Dados.append(cadastro)
    print("[bold green]Cadastro realizado com sucesso![/]")


def lista_cadastro():
    if not Dados:
        print("[red]Nenhum cadastro encontrado[/]")
        return
    
    tabela = Table(title="Lista de Cadastros")

    tabela.add_column("ID", style="cyan", justify="center")
    tabela.add_column("Nome", style="green")
    tabela.add_column("Idade", style="yellow")
    tabela.add_column("Sexo", style="magenta")
    tabela.add_column("Número", style="blue")

    for indice, pessoas in enumerate(Dados):
        tabela.add_row(
            str(indice + 1),
            pessoas["nome"],
            str(pessoas["idade"]),
            pessoas["sexo"],
            str(pessoas["numero"])
        )

    print(tabela)


def atualizar_cadastro(i, nome, idade, sexo, numero):
    if 0 <= i < len(Dados):
        Dados[i].update({
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "numero": numero
        })

        print("[green]Cadastro atualizado com sucesso![/]")

    else:
        print("[red]Atualização inválida[/]")


def excluir_cadastro(i):
    if 0 <= i < len(Dados):
        cadastro_excluido = Dados.pop(i)
        print(f"[green]Cadastro {cadastro_excluido['nome']} removido com sucesso![/]")
    else:
        print("[red]Erro ao remover[/]")



while True:
    conteudo = "Opções"
    conteudo += "\n1. Criar novo cadastro"
    conteudo += "\n2. Lista cadastro"
    conteudo += "\n3. Atualizar cadastro"
    conteudo += "\n4. Excluir cadastro"
    conteudo += "\n5. Sair"
    menu = Panel(conteudo,title="Sistema CRUD", width=28)

    print(menu)

    try:
        escolha = int(input("Digite uma Opção: "))
    except ValueError:
        print("[red]Digite apenas números![/]")
        continue

    if escolha == 1:
        nome = str(input("Digite seu Nome: ")).strip()
        while True:
            try:
                idade = int(input("Digite sua Idade: "))
                break
            except ValueError:
                print("[red]Digite apenas número[/]")
                
        sexo = ''
        while sexo not in ["M", "F"]:
            sexo = str(input("Digite seu sexo[F|M]: ")).strip().upper()
        numero = int(input("Digite seu Número: "))
        criar_cadastro(nome, idade, sexo, numero)
    elif escolha == 2:
        lista_cadastro()
    elif escolha == 3:
        indice = int(input("Digite o indice para altera: "))-1
        nome_novo = str(input("Novo nome:")).strip()
        idade_nova = int(input("Idade nova: "))
        sexo_novo = str(input("Sexo novo: ")).strip().upper()
        numero_novo = int(input("Número novo: "))
        atualizar_cadastro(indice, nome_novo, idade_nova, sexo_novo, numero_novo)
    elif escolha == 4:
        indice = int(input("Qual indice deseja excluir: "))-1
        excluir_cadastro(indice)
    elif escolha == 5:
        print("Sistema Cadastro encerrado")
        break
    else:
        print("[red]Digite um Opção válida[/]")
    