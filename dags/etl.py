import requests
import pandas as pd
from sqlalchemy import create_engine

def extrair_data():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame([{
        'moeda': k,
        'valor': float(v['bid'])
    } for k, v in data.items()])
    return df

def transformar_data(df):
    df['valor'] = df['valor'].round(2)
    return df

def carregar_data(df):
    engine = create_engine('postgresql://airflow:airflow@postgres:5432/airflow')
    df.to_sql('cotacao_moedas', engine, if_exists='replace', index=False)

def run_etl():
    df = extrair_data()
    df = transformar_data(df)
    carregar_data(df)
