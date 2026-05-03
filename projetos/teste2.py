usuario = []

def adicionar_usuario(nome):
    usuario.append(nome)

def lista_usuario():
    for num, pessoa in enumerate(usuario):
        print(f"{num+1} = {pessoa}")

adicionar_usuario("jailson")
adicionar_usuario("paulo")
adicionar_usuario("maria")
adicionar_usuario("jose")
adicionar_usuario("ana")
lista_usuario()