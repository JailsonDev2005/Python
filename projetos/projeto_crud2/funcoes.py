#MELHORA A SAIDA DO TERMINAL
from rich import print
#CAIXAS PAINÉIS ESTILIZADAS NO TERMINAL
from rich.panel import Panel
#TABELAS BONITAS E ORGANIZADAS
from rich.table import Table
#PERMITE USAR O BANCO DE DADOS SQLITE
import sqlite3

import hashlib


#CRIA UM BANCO DE DADOS
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

#CRIA TABELA NO BANCO USANOD O MÓDULO
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               email TEXT NOT NULL,
               senha TEXT NOT NULL
               )
""")


#SALVA AS ALTERAÇOES NO BANCO DE DADOS
conn.commit()


#CRIA UM MENU NO TERMINAL
def menu():

    conteudo = "Cadastro"
    conteudo += "\n1. Criar cadastro"
    conteudo += "\n2. Ler cadastro"
    conteudo += "\n3. Atualizar cadastro"
    conteudo += "\n4. Deletar cadastro"
    conteudo += "\n5. Sair"
    menu = Panel(conteudo, title="Sistema Cadastro", width=28, expand=False)
    print(menu)


#INSERE UM USURÁRIO NA TABELA
def criar_usuario(nome, idade, email, senha):

    senha_hash = hash_senha(senha)

    cursor.execute(
        "INSERT INTO usuarios (nome, idade, email, senha)    VALUES (?, ?, ?, ?)",
        (nome, idade, email, senha)
    )

    conn.commit()

    print("[green]Cadastro realizado com sucesso![/]")


#MOSTRA OS USUÁRIOS DE FROMA ORGANIZADA
def listar_usuario():
    cursor.execute("SELECT id, nome, idade, email FROM usuarios")

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

#ATUALIZAR OS DADOS DE UM USUÁRIO JA EXISTENTE
def atualizar_usuario(id_usuario, nome, idade, email, senha):

    senha_hash = hash_senha(senha)
    
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


#REMOVE UM USUÁRIO DO BANCO DE DADOS
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

#GARANTI QUE O USUÁRIO DIGITE UM NÚMERO INTEIRO VÁLIDO
def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("[red]Digite apenas números[/]")



def fechar_conexao():
    conn.close()