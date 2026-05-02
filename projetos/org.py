import os
import shutil

pasta_origem = r"C:\Users\Docs\Downloads\ex"

categorias = {
    'imagens': ['.png', '.jpg', '.gif'],
    'Documentos': ['.pdf', '.xml'],
    'Instaladores': ['.exe', '.msi']
}

for categoria in categorias:
    caminho_destino = os.path.join(pasta_origem, categoria)
    os.makedirs(caminho_destino, exist_ok=True)

for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    _, extensao = os.path.splitext(arquivo)

    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            destino = os.path.join(pasta_origem, categoria, arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f"Movido: {arquivo} -> {categoria}")
            break