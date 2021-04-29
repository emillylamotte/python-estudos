# Plotagem de gráficos - Histograma e Mapa de calor

Este algoritmo foi desenvolvido durante a imersão de desenvolvimento em Python da Hashtag Treinamentos, entre os dias 26 e 29/04/2021. 

## Tecnologias utilizadas:

- Extensão Jupyter no VSCode;
- Bibliotecas: pandas, seaborn e matplotlib.

**Tabela de dados disponibilizada pela Hashtag Treinamentos em: [https://drive.google.com/drive/folders/1KSZ4UDM7BQcVbxHK3Z-NeZec6BRcaslH](https://drive.google.com/drive/folders/1KSZ4UDM7BQcVbxHK3Z-NeZec6BRcaslH) 

É necessário realizar o download da base de dados e é importante que esse arquivo esteja no mesmo diretório do arquivo .ipynb. 

## Sobre o projeto

O projeto desenvolvido utiliza a biblioteca "pandas" para realizar a manipulação de dados de um arquivo .csv e as bibliotecas "seaborn" e "matplotlib" para plotar os gráficos das informações obtidas. O objetivo do algoritmo é auxiliar na análise de informações de investimento (valor pago) em diferentes meios de propaganda e seu retorno nas vendas do serviço.

Em primeira análise, plotamos a tabela de dados para visualizar as informações em questão:

```python
import pandas as pd 
tabela = pd.read_csv("advertising.csv")
display(tabela)
```

Resultando como saída:
<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116621164-254cd180-a919-11eb-957e-dfd5eedd3dc3.PNG" width="200"/>
</p>

(Valores de investimento de TV, Radio e Jornal em milhares; Valor retornado nas vendas em milhões)

Em seguida começamos a etapa de tratamento de dados, visualizando as informações da tabela em busca de incompatibilidade de tipos ou de informações faltando:

```python
display(tabela.info())
```

É possível visualizar na saída obtida que não há a necessidade de realizar um tratamento nos dados.
<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116621310-5cbb7e00-a919-11eb-9478-11929daeefcc.PNG" width="200"/>
</p>

Após essas etapas, começamos a plotagem do histograma e do mapa de calor (gráfico de correlação):

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

sns.pairplot(tabela)
plt.show()
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
```

É possível visualizar na saída um histograma que relaciona os meios de propaganda com o número de vendas, além da relação entre os meios.
<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116621426-84124b00-a919-11eb-8d93-3149f42c6ffe.PNG" width="450"/>
</p>

Analisando o histograma, observa-se que a propaganda na TV é a mais eficiente para o aumento das vendas. 

Além disso, será apresentado na saída um Mapa de Correlação entre os meios de propaganda e vendas. Sendo possível analisar quais meios são mais eficientes quando utilizados ao mesmo tempo, quanto mais próximo de 1, maior a correlação entre os dados.
<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116621605-d2274e80-a919-11eb-96e4-2b5084c4f26f.PNG" width="300"/>
</p>

## Conclusão

O algoritmo desenvolvido é capaz de retirar informações de uma base de dados, realizar o tratamento desses dados conforme a demanda observada e plotar os gráficos dessas informações, permitindo uma análise mais fácil do retorno obtido pelo investimento. 
<br><br><br>
✔️ Por Emilly Lamotte, Abril/2021
