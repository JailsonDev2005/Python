from database import cursor, conn
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def criar_usuario(nome, idade, email, senha):
    senha_hash = hash_senha(senha)

    cursor.execute("""
        INSERT INTO usuarios (nome, idade, email, senha)
        VALUES (?, ?, ?, ?)
    """, (nome, idade, email, senha_hash))

    conn.commit()

    return {"message": "Usuário criado com sucesso"}


def listar_usuarios():
    cursor.execute("SELECT id, nome, idade, email FROM usuarios")
    usuarios = cursor.fetchall()

    return [
        {"id": u[0], "nome": u[1], "idade": u[2], "email": u[3]}
        for u in usuarios
    ]


def deletar_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conn.commit()

    return {"message": "Usuário deletado"}