from sklearn.preprocessing import StandardScaler
import streamlit as st 
import pandas as pd
import pickle 

st.header("Predição de Churn - TELCO")
st.write("Churn rate, ou simplesmente churn, é uma métrica de negócios que mede a taxa de clientes," \
"assinantes ou usuários que deixam de fazer negócios com uma empresa ou cancelam seus serviços em um determinado" \
"período de tempo. Em português, o termo pode ser traduzido como taxa de rotatividade ou taxa de evasão de clientes.")


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

st.subheader("Dados de input do modelo")

st.write("Dados brutos")
st.write(df)

num = ["tenure", "MonthlyCharges", "TotalCharges"]

df['OnlineSecurity_No'] = df['OnlineSecurity'].apply(lambda x: 1 if x == "No" else 0)
df['OnlineSecurity_Yes'] = df['OnlineSecurity'].apply(lambda x: 1 if x == "Yes" else 0)
df['OnlineSecurity_No internet service'] = df['OnlineSecurity'].apply(lambda x: 1 if x == "No internet service" else 0)

df['TechSupport_No'] = df['TechSupport'].apply(lambda x: 1 if x == "No" else 0)
df['TechSupport_Yes'] = df['TechSupport'].apply(lambda x: 1 if x == "Yes" else 0)
df['TechSupport_No internet service'] = df['TechSupport'].apply(lambda x: 1 if x == "No internet service" else 0)


df_categorical = df.drop(["TechSupport", "OnlineSecurity"]+num, axis=1)

load_scaler = pickle.load(open("assets/scaler.pkl", 'rb'))
df_std = pd.DataFrame(load_scaler.transform(df[num]), columns=num)
df_std['charges_ratio'] = df_std['tenure']*df_std['MonthlyCharges'] / (df_std['TotalCharges'] + 1)

df_processed = pd.concat([df_std, df_categorical], axis=1)


df_processed = df_processed[[
    'tenure','MonthlyCharges','TotalCharges','OnlineSecurity_No',
    'OnlineSecurity_No internet service','OnlineSecurity_Yes','TechSupport_No',
   'TechSupport_No internet service','TechSupport_Yes','charges_ratio'
   ]]

st.write("Dados tratados")
st.write(df_processed)

load_model = pickle.load(open("assets/churn_tree_model.pkl", 'rb'))
predictions = load_model.predict(df_processed)
pred = round(predictions[0],2)

if pred == 0:
    st.write("Para este cliente a previsão é de: **NÃO CHURN** ")
else:
    st.write("Para este cliente a previsão é de: **CHURN** ")