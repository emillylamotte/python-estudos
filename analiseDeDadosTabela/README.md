# Análise de dados de uma tabela

Este algoritmo foi desenvolvido durante a imersão de desenvolvimento em Python da Hashtag Treinamentos, entre os dias 26 e 29/04/2021. 

## Tecnologias utilizadas:

- Extensão Jupyter no VSCode;
- Bibliotecas: pandas e plotly.

**tabela de dados disponibilizada em: [https://www.kaggle.com/sakshigoyal7/credit-card-customers](https://www.kaggle.com/sakshigoyal7/credit-card-customers)

***em português (disponibilizado pela Hashtag Treinamentos): [https://drive.google.com/drive/folders/1w3TmCcQPoc7ew1CXmwwEUpWeHJzJQqGZ](https://drive.google.com/drive/folders/1w3TmCcQPoc7ew1CXmwwEUpWeHJzJQqGZ)

É necessário realizar o download da base de dados e que esse arquivo esteja no mesmo diretório do arquivo .py. 

## Sobre o projeto:

O projeto desenvolvido utiliza a biblioteca "pandas" para realizar a manipulação de dados de um arquivo .csv e a biblioteca "plotly" para plotar os gráficos das informações obtidas. O objetivo do algoritmo é auxiliar na análise de dados de cancelamento de um serviço, neste caso de provedor de internet.  

Em primeira análise, plotamos a tabela de dados para reconhecer possíveis problemas como linhas/colunas vazias e colunas que não serão úteis na análise, como mostrado na figura abaixo:

<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116484091-bc088800-a85e-11eb-9922-6b6cb675ca16.PNG" width="600"/>
</p>

Podemos observar que a coluna "Unnamed" não será útil na análise, pois não traz nenhuma informação. Por isso, o algoritmo exclui essa coluna.

Após, inicia-se a etapa de tratamento de dados. Verificamos se os tipos de dados correspondem a informação apresentada e se não existem elementos/colunas vazios. Por exemplo, foi detectado que a coluna "TotalGasto" foi apresentada como um texto ao invés de um número e que existem colunas com informações vazias, isso pode atrapalhar a análise dos dados.

O algoritmo corrige esse problema convertendo o dado "TotalGasto" para número e excluindo elementos vazios da minha base de dados, que após as modificações encontra-se assim: 

<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116484141-d478a280-a85e-11eb-8fdf-bc97b9545b13.PNG" width="450"/>
</p>

Depois que esse tratamento de dados é realizado, iniciamos a análise. Primeiro, o algoritmo verifica qual a porcentagem de cancelamentos do serviço (26.6%), como mostra a figura abaixo:

<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116484161-dfcbce00-a85e-11eb-9608-fe8091083ad6.PNG" width="300"/>
</p>

Feito isso, o algoritmo inicia a plotagem de gráficos contendo todas as colunas da base de dados, juntamente com a  taxa de cancelamento em cada uma delas, permitindo que a análise possa ser realizada mais afundo e apontando quais os problemas que estão gerando cancelamento. Por exemplo, no gráfico da coluna "MesesComoCliente" X Taxa de cancelamento ("Churn") mostrado abaixo podemos observar que a taxa de cancelamento é extremamente alta nos primeiros meses de serviço prestado e pode-se começar a pensar em soluções para esse problema.

<p align="center"> 
<img src="https://user-images.githubusercontent.com/79487290/116484176-e8bc9f80-a85e-11eb-8dd9-9a718c13f776.PNG" width="500"/>
</p>

## Conclusão

O algoritmo desenvolvido é capaz de retirar informações de uma base de dados, realizar o tratamento desses dados conforme a demanda observada e plotar os gráficos dessas informações, permitindo uma análise mais fácil do problema. 

✔️ Por Emilly Lamotte, Abril/2021
