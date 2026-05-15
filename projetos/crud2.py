from rich import print
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


dados = []

def menu():

    print("-"*30)
    print("Cadastro")
    print("1. Criar Cadastro")
    print("2. Ler cadastro")
    print("3. Atualizar cadastro")
    print("4. Deletar cadastro")
    print("5. Sair")
    print("-"*30)


def criar_usuario():
    pass


def listar_usuario():
    pass


def atualisar_usuario():
    pass


def deletar_usuario():
    pass


def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas números")





while True:

    menu()

    escolha = ler_inteiro("Escolha uma Opçâo: ")


    if escolha == 1:

        nome = str(input("Qual seu nome: "))
        idade = ler_inteiro("Qual sua idader: ")
        email = str(input("Qual seu email: "))
        senha = input("Qual sua senha: ")

        cursor.execute(
            "INSERT INTO usuarios (nome, idade, email, senha)    VALUES (?, ?, ?, ?)",
            (nome, idade, email, senha)
        )

        conn.commit()

        print("Cadastro realizado com sucesso!")


    elif escolha == 2:

        cursor.execute("SELECT * FROM usuarios")

        usuarios = cursor.fetchall()

        print("Lista de Usuários")

        for usuario in usuarios:
            print(f"ID: {usuario[0]}")
            print(f"Nome: {usuario[1]}")
            print(f"Idade: {usuario[2]}")
            print(f"Email: {usuario[3]}")
            print(f"Senha: {usuario[4]}")


    elif escolha == 3:

        id_usuario = int(input("Digite o ID do usuário: "))
        novo_nome = str(input("Novo nome: "))
        nova_idade = ler_inteiro("Nova idade: ")
        novo_email = str(input("Novo email: "))
        novo_senha = input("Nova senha: ")

        cursor.execute("""
            UPDATE usuarios
            SET nome = ?, idade = ?, email = ?, senha = ?
            WHERE id = ?
        """, (novo_nome, nova_idade, novo_email, novo_senha, id_usuario))

        conn.commit()

        print("Cadastro atualizado!")
    

    elif escolha == 4:

        id_usuario = ler_inteiro("Digite o ID para deletar: ")

        cursor.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (id_usuario,)
        )

        conn.commit()

        print("Cadastro deletado!")


    elif escolha == 5:

        print("Saindo do sistema...")
        break

    else:

        print("Opção inválida!")

conn.close()