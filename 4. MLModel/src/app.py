import streamlit as st 
import pandas as pd
import pickle 
from core import config, ASSETS_PATH
from preprocess import prepare_data

st.header("Predição de Churn - TELCO")
st.write("Churn rate, ou simplesmente churn, é uma métrica de negócios que mede a taxa de clientes," \
"assinantes ou usuários que deixam de fazer negócios com uma empresa ou cancelam seus serviços em um determinado" \
"período de tempo. Em português, o termo pode ser traduzido como taxa de rotatividade ou taxa de evasão de clientes.")

## -----------
## BIG NUMBERS
## -----------

a, b, c = st.columns(3)
a.metric("**Clientes Ativos**", "215k", "-15%")
b.metric("**Churn Rate**", "25%", "12%")
c.metric("**LTV médio**", "R$1500", "3%")

## -----------
## USER INPUT FEATURES
## -----------
st.sidebar.header("Selecione as características do cliente")

def user_input_features():
    tenure = st.sidebar.slider("tenure", 0, 50, 100)
    MonthlyCharges = st.sidebar.slider("MonthlyCharges", 10, 75, 150)
    TotalCharges = st.sidebar.slider("TotalCharges", 15, 5000, 10000)
    OnlineSecurity = st.sidebar.selectbox("OnlineSecurity", ("Yes", "No", "No internet service"))
    TechSupport = st.sidebar.selectbox("TechSupport", ("Yes", "No", "No internet service"))
    
    data = {"tenure": tenure,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges,
            "OnlineSecurity": OnlineSecurity, 
            "TechSupport": TechSupport}

    features = pd.DataFrame(data, index=[0])
                                           
    return features

df = user_input_features()

## -----------
## DATA PROCESS
## -----------

st.subheader("Dados de input do modelo")
st.write("Dados brutos")
st.write(df)

print(type(df))

df_processed = prepare_data(df)

st.write("Dados tratados")
st.write(df_processed)

## -----------
## MODEL
## -----------

load_model = pickle.load(
    open(config.ml_config.trained_model_file, 'rb'))
predictions = load_model.predict(df_processed)
pred = round(predictions[0],2)

if pred == 0:
    st.write(":white_check_mark: NÃO PROPENSO AO CHURN")
else:
    st.write(":x: PROPENSO AO CHURN")