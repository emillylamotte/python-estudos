#Importar a base de dados
import pandas as pd 
tabela = pd.read_csv("advertising.csv")
display(tabela)

#Visualização das informações para possível tratamento de dados
display(tabela.info())

#Gerando gráficos
import seaborn as sns #cria o gráfico
import matplotlib.pyplot as plt #mostra o gráfico

sns.pairplot(tabela)# grafico que une os tipos de propaganda com as vendas
plt.show()
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
