# DBSeeker

## Buscador de dados SQL Server

Bem vindos ao meu script de busca de dados em bancos SQL Server.

Este script foi feito em python, utilizando a biblioteca "pyodbc"

## Guia de uso
- Instale o python na versão 3.9.

- No terminal, crie seu ambiente virtual "py -m venv venv".

- Instale a biblioteca pyodbc, "pip install pyodbc".

- Agora, mude os valores das variáveis "HOST, USER, PASSWORD E DATABASE", para os valores referentes ao seu banco de dados.

- Execute o script, "py dbseeker.py".

## Observação:

Este deve ser utilizado da forma que está, apenas em bancos de dados pequenos. Você pode modifica-lo para buscar menos colunas, 
ou criar mais indices de buscas, deixando a consulta mais leve. Em bancos de dados muito grandes, é possível que ocorra travamento,
por isso, modifique-o conforme sua necessidade.

Você pode criar novas variáveis, ou setar como string, novos parâmetros, na linha 48, onde se encontra a consulta.

By: DavidFintt

