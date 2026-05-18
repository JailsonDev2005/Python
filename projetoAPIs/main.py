#IMPORTA O FASTAPI
from fastapi import FastAPI, HTTPException
#SERVE PARA DEFINIR O FORMATO DOS DADOS
from pydantic import BaseModel
#AJUDAR NA TIPAGEM
from typing import List, Optional

#CRIAR API
app = FastAPI(title="API de Tarefas")

#uvicorn projetoAPIs.main:app --reload

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

#BUSCAR TAREFA POR ID
@app.get('tarefa/{tarefa_id}', response_model=Tarefa)
async def obter_tarefa(tarefa_id: int):
    for t in db_tarefas:
        if t.id == tarefa_id:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

#ROTA PARA ALTERA
@app.put('/tarefas/{tarefas_id}', response_model=Tarefa)
async def atualizar_tarefa(tarefa_id: int, tarefa_atualizar: Tarefa):
    for index, t in enumerate(db_tarefas):
        if t.id ==tarefa_id:
            tarefa_atualizar.id = tarefa_id

            db_tarefas[index] = tarefa_atualizar

            return tarefa_atualizar
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrado")


#ROTA PARA DELETAR
@app.delete('/tarefas/{tarefas_id}', status_code=204)
async def delete_tarefa(tarefa_id: int):
    for t in db_tarefas:
        if t.id == tarefa_id:
            db_tarefas.remove(t)
            return
    raise HTTPException(status_code=404)