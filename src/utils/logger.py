import logging
from datetime import datetime
import os

def get_logger(name: str = "databricks_app", log_level=logging.INFO):
    """Cria um logger configurado com formato padrão de arquivo."""

    # Diretório padrão para logs
    log_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_dir, exist_ok=True)

    # Nome do arquivo de log com data/hora
    log_file = os.path.join(log_dir, f"{name}_{datetime.now().strftime('%Y%m%d_%H%MS')}.log")

    # Configuração básica de logging
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Evita duplicar o handlers se o logger já existir
    if not logger.hanlders:
        # Formato de log
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m_%d %H:%M:%S"
        )

        # hanlder para arquivo
        file_handler = logging.FileHandler(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Handler para console (Databricks exibe no output)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return loggger    