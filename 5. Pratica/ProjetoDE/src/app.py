import utils as utils
import logging
from core import configs

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info("Iniciando processo de ingestão")
    try:
        df = utils.ingestion(configs)
    except:
        logging.error("Erro de ingestão de dados")
    try:
        utils.preparation(df, configs)
        logging.info("Fim do processo de ingestão")
    except:
        logging.error("Erro de preparação")