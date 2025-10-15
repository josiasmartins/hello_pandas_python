import pandas as pd

def gerar_relatorio():
    dados = {
        'Nome': ['Rafa', 'Ana'],
        'Idade': [23, 35],
        'Cidade': ['SP', 'RJ']
    }
    df = pd.DataFrame(dados)
    print('Relatório de pessoas')
    print(df)

if __name__ == "__main__": 
    gerar_relatorio()    