import utils as utils
import logging
from config import configs


config_file = configs
logging.basicConfig(level=logging.INFO)

logging.info("Iniciando a ingestão")
utils.ingestion(configs, config_file)
utils.preparation(configs, config_file)
    