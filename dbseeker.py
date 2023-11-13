import pyodbc
import os
import sys

#Variáveis utilizadas
table_list = []
column_list = []
count_table = 0
current_table = ''
dict_table_columns = {}
where_parameter = ''

#Configuração da conexão
host = 'HOST'
user = 'USER'
password = 'PASS'
database = 'DB'
conn = pyodbc.connect(f'DRIVER={{SQL Server}}; Server={host};DATABASE={database};UID={user};PWD={password}')

cursor = conn.cursor()

tables_db = cursor.tables(tableType='TABLE')

#Adicionar resultados a lista "table_list". Como usei um banco de dados TOTVS, eu usei um filtro "len" para trazer apenas as tabelas padrões, com valores inputados pelos usuários.
for t in tables_db:
    if len(t[2]) == 6:
        table_list.append(t[2])

#Percorrer as tabelas adicionadas a "table_list" e em seguida, percorrer a coluna de cada uma, e criar um dict com os valores. 
for lt in table_list:
    if count_table == 0:
        current_table = lt
    if current_table != lt:
        column_list.clear()
        current_table = lt
    columnsIndex = cursor.columns(table=table_list[count_table])
    for c in columnsIndex:        
        column_name = c.column_name
        column_list.append(column_name)
    
    dict_table_columns.update({current_table: column_list.copy()})
    if count_table < len(table_list):
        count_table += 1

#Percorrer o dicionario e realizar as consultas.
for k, v in dict_table_columns.items():
    for b in v:
        final = cursor.execute(f"SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED SELECT {b} FROM {k} WHERE {b} LIKE '%{where_parameter}%' ")
        row_result = final.fetchall()

        if len(row_result) > 0:
            print(f'O Registro está na tabela {k}, na coluna {b}') 
