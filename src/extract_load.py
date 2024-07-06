# Import 
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Import das variaveis de ambiente

commodities = ['CL=F', 'GC=F', 'SI=f']
def buscar_dados(simbolo, periodo= '5d' , intervalo= '1d'):
    
    ticker = yf.Ticker('')
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_todos_dados(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados(commodities)
    print(dados_concatenados)

# pegar cotação dos meus ativos

# concatenar ativos (1..2..3) -> (1) 

# Salvar banco de dados