import pandas as pd
import pickle 
import numpy as np
from pydantic import ValidationError
from core import config, MultipleDataSchema


def validate_inputs(raw_data: pd.DataFrame):
    """Validade columns and data type follow the model requirements """

    errors = None
    features = config.data_config.quali_variables + config.data_config.quanti_variables
    data = raw_data[features+ [config.ml_config.target]]

    try:
        MultipleDataSchema(inputs=data.replace({np.nan: None}).to_dict(orient="records"))
    except ValidationError as error:
        errors = error.json()
    
    return data, errors


def prepare_data(df):

    try:
        load_preprocessor = pickle.load(
            open(config.ml_config.preprocess_model_file, 'rb'))
    except Exception as expection_error:
        #todo: gravar erro
        pass

    data, errors = validate_inputs(df)
    if  not errors:

        df_processed = load_preprocessor.transform(data)
        nomes_quali = list(load_preprocessor.named_transformers_['quali'].get_feature_names_out(
            config.data_config.quali_variables)) 
        nomes_variaveis =  list(config.data_config.quali_variables) + nomes_quali

        #acrescentar um tratamento snake case para o nomde das variáveis aqui

        X_tratada = pd.DataFrame(df_processed, columns=nomes_variaveis)

        vars = list(set(MultipleDataSchema.inputs) - set(nomes_variaveis))
        if len(vars) > 0:
            for col in vars:
                X_tratada[col] = 0

    return X_tratada[MultipleDataSchema.inputs]
