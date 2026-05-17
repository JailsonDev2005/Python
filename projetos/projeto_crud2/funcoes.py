from rich import print
from rich.panel import Panel
from rich.table import Table
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               email TEXT NOT NULL,
               senha TEXT NOT NULL
               )
""")

conn.commit()

def menu():

    conteudo = "Cadastro"
    conteudo += "\n1. Criar cadastro"
    conteudo += "\n2. Ler cadastro"
    conteudo += "\n3. Atualizar cadastro"
    conteudo += "\n4. Deletar cadastro"
    conteudo += "\n5. Sair"
    menu = Panel(conteudo, title="Sistema Cadastro", width=28, expand=False)
    print(menu)



def criar_usuario(nome, idade, email, senha):


    cursor.execute(
        "INSERT INTO usuarios (nome, idade, email, senha)    VALUES (?, ?, ?, ?)",
        (nome, idade, email, senha)
    )

    conn.commit()

    print("[green]Cadastro realizado com sucesso![/]")


def listar_usuario():
    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    if not usuarios:
        print("[yellow]Nenhum usuário cadastrado[/]")
        return

    table = Table(title="Lista de Usuários")
    table.add_column("ID", style="cyan")
    table.add_column("Nome", style="green")
    table.add_column("Idade", style="yellow")
    table.add_column("Email", style="magenta")

    for usuario in usuarios:
        table.add_row(
            str(usuario[0]),
            usuario[1],
            str(usuario[2]),
            usuario[3]
        )

    print(table)


def atualizar_usuario(id_usuario, nome, idade, email, senha,):
    
    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, idade = ?, email = ?, senha = ?
        WHERE id = ?
    """, (nome, idade, email, senha, id_usuario))

    conn.commit()

    if cursor.rowcount == 0:
        print("[red]Usuário não encontrado[/]")
    else:
        print("[green]Cadastro atualizado![/]")



def deletar_usuario(id_usuario):

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id_usuario,)
    )

    conn.commit()


    if cursor.rowcount == 0:
        print("[red]Usuário não encontrado[/]")
    else:
        print("[green]Cadastro deletado![/]")


def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("[red]Digite apenas números[/]")

