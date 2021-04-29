#Importar a base de dados
import pandas as pd 

tabela = pd.read_csv("advertising.csv")
display(tabela)

#Visualização dos dados para verificar a necessidade de tratamento
display(tabela.info())

#Geração dos gráficos
import seaborn as sns
import matplotlib.pyplot as plt 

sns.pairplot(tabela)
plt.show()
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
