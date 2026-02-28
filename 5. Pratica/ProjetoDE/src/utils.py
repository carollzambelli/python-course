import os
import pandas as pd
from datetime import datetime
import awswrangler as wr   
import uuid


class Saneamento:
    
    def __init__(self, data, configs):
        self.data = data
        self.colunas = configs["metadados"]['nome_original']
        self.colunas_new = configs["metadados"]['nome']
        self.tipos = configs["metadados"]['tipos']  

    def select_rename(self):
        self.data = self.data.loc[:, self.colunas] 
        for i in range(len(self.colunas)):
            self.data.rename(columns={self.colunas[i]:self.colunas_new[i]}, inplace = True)

    def tipagem(self):
        for col in self.colunas_new:
            tipo = self.tipos[col]
            if tipo == "int":
                tipo = self.data[col].astype(int)
            elif tipo == "float":
                self.data[col].replace(",", ".", regex=True, inplace = True)
                self.data[col] = self.data[col].astype(float)
            elif tipo == "date":
                self.data[col] = pd.to_datetime(self.data[col]).dt.strftime('%Y-%m-%d')
        return self.data
    
def save_bucket(df, configs, step):
    bucket = configs["bucket"][step]
    df['load_date'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    file = f"cadastro_{step}_{str(uuid.uuid4())}.csv"
    wr.s3.to_csv(
        df=df,
        path=f"{bucket}{file}",
        header=False,
        sep=";",
        index=False
    )

def read_athena(query):
    df = wr.athena.read_sql_query(query, database='database')
    return df

def error_handler(exception_error, stage, configs):
    log = [stage, type(exception_error).__name__, exception_error,datetime.now()]
    logdf = pd.DataFrame(log).T
    save_bucket(logdf, configs, step="logs")

