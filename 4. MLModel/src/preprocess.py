import pandas as pd
import pickle 
import numpy as np
import logging
from pydantic import ValidationError
from core import config, MultipleDataSchema


logging.basicConfig(filename="assets/app.log",
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validate_inputs(raw_data: pd.DataFrame):
    """Validade columns and data type follow the model requirements """
    
    try:
        MultipleDataSchema(inputs_raw=raw_data.replace({np.nan: None}).to_dict(orient="records"))
    except ValidationError as error:
        errors = error.json()
        logging.error(errors)
        raise ValueError("Inputs out of standard, review your raw data")
    
    return raw_data


def prepare_data(df):

    try:
        load_preprocessor = pickle.load(open(config.ml_config.preprocess_model_file, 'rb'))
    except Exception as expection_error:
        logging.error(expection_error)

    data = validate_inputs(df)
    
    df_processed = load_preprocessor.transform(data)
    nomes_quali = list(load_preprocessor.named_transformers_['quali'].get_feature_names_out(
        config.data_config.quali_variables)) 
    
    nomes_variaveis =  list(config.data_config.quanti_variables) + nomes_quali
    nomes_variaveis = [s.replace(" ", "_") for s in nomes_variaveis]
    
    X_tratada = pd.DataFrame(df_processed, columns=nomes_variaveis)

    vars_left = list(set(config.data_config.model_variables) - set(nomes_variaveis))

    if len(vars_left) > 0:
        for col in vars_left:
            X_tratada[col] = 0
    
    return X_tratada[config.data_config.model_variables]
    

if __name__ == '__main__':
    data = {"tenure": [100],
            "MonthlyCharges": [100],
            "TotalCharges": [10000],
            "OnlineSecurity": ['Yes'], 
            "TechSupport": ['Yes']}
    df = pd.DataFrame(data, index=[0])
    prepare_data(df)



    
    