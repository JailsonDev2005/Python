from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(order_router)
#uvicorn main:app --reload

# endpoint:
# /ordens

# Rest APIs
# Get -> leitura/pega
# Post -> envia/Criar
# Put/Patch -> edição
# Delete -> deletar