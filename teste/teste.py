import logging

logger = logging.getLogger("MeuSistemaLog")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("meu_app.log", mode="a")
formato = logging.Formatter("%(asctime)s - %(nome)s - %(levelname)s - %(messagen)s")

file_handler.setFormatter(formato)

logger.addHandler(file_handler)

logger.debug("isso é um debug")
logger.error("houve um error")