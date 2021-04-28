import pandas as pd

#Passo 1: Importar a base de dados
#Arquivo de dados e o .py devem estar no mesmo diretório
tabela_clientes = pd.read_csv("telecom_users.csv") 

#Passo 2: Visualizar a tabela, excluir colunas que não serão úteis na análise
tabela_clientes = tabela_clientes.drop("Unnamed: 0", axis=1) #excluindo a coluna Unnamed 
display (tabela_clientes) #exibir a tabela

#Passo 3: Tratamento de Dados
#Resolvendo Problemas de tipos de informação 
print (tabela_clientes.info()) #exibe a tabela e os tipos de dados contidos

#Corrigindo a coluna TotalGasto de formato texto para numero, se der erro preenche com vazio
tabela_clientes["TotalGasto"] = pd.to_numeric(tabela_clientes["TotalGasto"], errors="coerce")

#Problema de Valores vazios
tabela_clientes = tabela_clientes.dropna(how="all", axis=1) #exclui todas as colunas que possuem todos os valores vazios
tabela_clientes = tabela_clientes.dropna(how="any", axis=0) #exclui todas as linhas que tem algum valor vazio

#Parte 4: Visualizar novamente a tabela, observando a quantidade de pessoas que cancelaram o serviço
display(tabela_clientes["Churn"].value_counts()) #mostra a qtd de cancelamentos, qtd de sim/não
display(tabela_clientes["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #normalize mostra qtd em porcentagem, map formata o número exibido

#Passo 5: Gerar os gráficos para melhor análise do problema
import plotly.express as px #gera gráficos interativo

for coluna in tabela_clientes: #armazenando as colunas da tabela dentro da variavel coluna
    #gerando um gráfico para cada conjunto de informações/coluna
    grafico = px.histogram(tabela_clientes, x=coluna, color="Churn")#(de onde vem o dado, coluna em x, color deixa com cores alternadas)
    grafico.show()#exibe o grafico
