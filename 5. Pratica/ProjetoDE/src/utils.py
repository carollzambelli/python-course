import pandas as pd
import requests
import utils as utils

def ingestion(configs):
    """
    Função de ingestão dos dados
    Outputs: Salva base raw em local específico e retorna o nome do arquivo
    """
    return True


def validation_inputs(df, configs):
    """
    Função de validação dos dados antes de salvar no banco de dados
    Output: Se não estiver no padrão correto interrompe o processo e salva alerta em 
    um arquivo de logs. Se estiver correto, salva log com mensagem: 'Dados corretos'
    """
    return True


def preparation(df, configs):
    """
    Função de preparação dos dados: 
        - renomeia colunas,
        - Ajustas tipo dos dados
        - Remove caracter especial
    Outputs: Salva dados tratados em base sqlite no diretorio assets
    """

    #data = validate_inputs(df)

    return True

