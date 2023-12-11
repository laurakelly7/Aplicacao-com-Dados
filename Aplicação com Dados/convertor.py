import csv
import json

with open('listagem-de-filmes-brasileiros-lancados-1995-a-2021-3.csv', 'r', encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    next(reader)
    next(reader)
    dados = []

    for row in reader:
        dados.append({'Ano de Lançamento': row[0], 'Certificado de Produto Brasileiro (CPB)': row[1], 'Título': row[2], 'Direção': row[3], 'Gênero': row[4], 'Empresa Produtora Brasileira Majoritária': row[5], 'UF': row[6], 'Empresa Produtora Minoritária Brasileira': row[7], 'UF2': row[8], 'Distribuidora': row[9], 'Máximo de Salas': row[10], 'Público': row[11], 'Renda (R$)': row[12]})
    
with open('listagem-de-filmes-brasileiros-lancados-1995-a-2021-3.json', 'w', encoding='UTF-8') as json_file:
    json.dump(dados,  json_file, indent=4, ensure_ascii=False)

