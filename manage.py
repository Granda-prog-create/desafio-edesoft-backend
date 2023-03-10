import boto3
import pandas as pd
import psycopg2

from django.http import HttpResponse
from django.views.decorators.http import require_GET

s3 = boto3.client('s3')

@require_GET
def import_csv(request):
    bucket_name = request.GET.get('bucket_name')
    object_key = request.GET.get('object_key')

    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')

    # ler o arquivo CSV com o pandas
    df = pd.read_csv(content)

    # remover máscara de cpf e cnpj
    df['cpf'] = df['cpf'].str.replace(r'\D+', '')
    df['cnpj'] = df['cnpj'].str.replace(r'\D+', '')

    # formatar as datas
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    # conectar ao banco de dados
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='user',
        password='password',
        database='database'
    )

    # salvar os dados no banco
    cur = conn.cursor()
    for index, row in df.iterrows():
        cur.execute("""
            INSERT INTO tabela (cpf, cnpj, data)
            VALUES (%s, %s, %s)
        """, (row['cpf'], row['cnpj'], row['data']))
    conn.commit()
    cur.close()
    conn.close()

    # retornar a resposta HTTP
    return HttpResponse('Operação concluída com sucesso!')
