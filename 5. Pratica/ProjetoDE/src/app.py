import pandas as pd
import requests
import utils as utils
import logging
from config import configs


config_file = configs
logging.basicConfig(level=logging.INFO)


def ingestion():
    """
    Função de ingestão dos dados
    Outputs: Salva base raw em local específico e retorna o nome do arquivo
    """

    logging.info("Iniciando a ingestão")
    api_url = configs["URL"]
    try:
        response = requests.get(api_url, timeout=10).json()
        data = response['results']
    except Exception as exception_error:
        utils.error_handler(exception_error, 'read_api', config_file)
    df = pd.json_normalize(data)
    cols = [s.replace('.', '_') for s in df.columns]
    df.columns = cols
    utils.save_bucket(df, configs, step="raw")


def preparation():
    """
    Função de preparação dos dados: renomeia, tipagem, normaliza strings
    Arguments: file -> nome do arquivo raw
    Outputs: Salva base limpa em local específico
    """

    logging.info("Iniciando o saneamento")
    df = utils.read_athena(configs["prep_query"])
    san = utils.Saneamento(df, config_file)
    san.select_rename()
    logging.info("Seleção de dados")
    df = san.tipagem()
    logging.info("Tipagem dos dados")
    utils.save_bucket(df, configs, step="work")
    logging.info("Dados salvos")


def handler(event, context):
    ingestion()
    preparation()
    