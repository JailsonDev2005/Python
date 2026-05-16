from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
        essa é a rota padrão de pedidoss do nosso sistema, todas aas rota dos pedidos precisam de autenticação
    """
    return {"mensagem":"Você acessou a rota de pedidas"}