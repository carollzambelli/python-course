import pandas as pd
import pickle 


lista_X_quanti = ["tenure","MonthlyCharges","TotalCharges"]
lista_X_quali = ['OnlineSecurity','TechSupport']
model_vars = ['tenure', 'MonthlyCharges', 'TotalCharges', 'OnlineSecurity_No',
       'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
       'TechSupport_No', 'TechSupport_No internet service', 'TechSupport_Yes']

load_preprocessor = pickle.load(open("../assets/preprocessador.pkl", 'rb'))
load_model = pickle.load(open("../assets/lr_model.pkl", 'rb'))


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

    df_processed = load_preprocessor.transform(df[lista_X_quanti + lista_X_quali]) 
    nomes_quali = list(load_preprocessor.named_transformers_['quali'].get_feature_names_out(lista_X_quali)) 
    nomes_variaveis =  list(lista_X_quanti) + nomes_quali
    X_tratada = pd.DataFrame(df_processed, columns=nomes_variaveis)

    vars = list(set(model_vars) - set(nomes_variaveis))
    if len(vars) > 0:
        for col in vars:
            X_tratada[col] = 0

    return X_tratada[model_vars]
