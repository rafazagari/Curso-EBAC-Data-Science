import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sns.set()

#Utilizando a função criada na aula anterior
def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada', meses=None):
    if opcao == 'nada':
        if meses:
            filtered_df = df[df['DTNASC'].str[:7].isin(meses)]
            pd.pivot_table(filtered_df, values=value, index=index, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None

def main():
    # Lendo os dados a partir da database
    sinasc = pd.read_csv('SINASC_RO_2019.csv')
    
    # Definindo os meses desejados
    meses_escolhidos = {
        'MAR': '2019-03',
        'ABR': '2019-04',
        'MAI': '2019-05',
        'JUN': '2019-06',
        'JUL': '2019-07'
    }
    
    # Criando diretório para os gráficos
    if not os.path.exists('graficos'):
        os.mkdir('graficos')
    
    for mes_abrev, mes_referencia in meses_escolhidos.items():
        # Criando diretório para os meses
        mes_dir = os.path.join('graficos', mes_referencia)
        if not os.path.exists(mes_dir):
            os.mkdir(mes_dir)
        
        # Chamando a função para plotar os gráficos
        plota_pivot_table(
            sinasc, 
            value='PESO', 
            index='IDADEMAE', 
            func='mean', 
            ylabel='Peso recém-nascido', 
            xlabel='Idade da Mãe', 
            opcao='unstack', 
            meses=[mes_referencia]
        )
        
        # Salvando o gráfico no diretório de cada mês
        plt.savefig(os.path.join(mes_dir, 'grafico.png'))
        plt.close()
    
    print("Gráficos gerados!")

if __name__ == "__main__":
    main()
