#IMPORTA O FASTAPI
from fastapi import FastAPI, HTTPException
#SERVE PARA DEFINIR O FORMATO DOS DADOS
from pydantic import BaseModel
#AJUDAR NA TIPAGEM
from typing import List, Optional

#CRIAR API
app = FastAPI(title="API de Tarefas")

#MODELO DE DADOS
class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    conlcuida: bool = False

#BANCO EM MEMORIA
db_tarefas = []

#ROTA PARA LISTAR TODAS AS TAREFAS
@app.get('/tarefas', response_model=List[Tarefa])
async def listar_tarefas():
    return db_tarefas

#ROTA PARA CRIAR TAREFA
@app.post('/tarefa', response_model=Tarefa, status_code=201)
async def criar_tarefa(tarefa: Tarefa):
    tarefa.id = len(db_tarefas) + 1
    db_tarefas.append(tarefa)
    return tarefa


