import yfinance as yf
import pandas as pd


commodities = ['CL=F','CG=F','SI=F']

def buscar_dados(simbolo,periodo='5y',intervalo='1d'):
    ticker = yf.ticker('CL=F')
    dados = ticker.history(period=periodo,interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commdities():
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commdities(commodities)
    print(dados_concatenados)


