from fastapi import FastAPI
from crud import criar_usuario, listar_usuarios, deletar_usuario

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API funcionando"}

# CREATE
@app.post("/usuarios")
def create_usuario(nome: str, idade: int, email: str, senha: str):
    return criar_usuario(nome, idade, email, senha)

# READ
@app.get("/usuarios")
def get_usuarios():
    return listar_usuarios()

# DELETE
@app.delete("/usuarios/{id_usuario}")
def delete_usuario(id_usuario: int):
    return deletar_usuario(id_usuario)