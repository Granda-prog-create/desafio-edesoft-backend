# Aplicação de leitura de dados 

Nessa aplicação foi utilizado o Django Framework por possibilitar a criação de ambientes virtuais e locais. 

# Bibliotecas instaladas

Django (framework)

psycopg2-binary (lib para banco de dados PostgreSQL)

gunicorn (para rodar o projeto)

dj-static (arquivos estáticos)

django-stdimage (para trabalhar com imagens)

pandas (ler CSV)

boto3 (Facilitar a integração da aplicação, biblioteca ou script Python aos serviços da AWS, incluindo Amazon S3, Amazon EC2 e Amazon DynamoDB, entre outros.)

# Boas práticas de instalação

É possível isntalar todas as bibliotecas com um único comando. Digite no terminal: pip install django psycopg2-binary gunicorn dj-static django-stdimage pandas boto3 

# Requirements

No arquivo requirementes.txt está todas as bibliotecas e versões instaladas. 

Para ter esse arquivo na aplicação, digite na pasta raiz do projeto: pip freeze > requeriments.text 

# Criar o projeto django

django-admin startproject edesoft . 

# Aplicação core

django-admin startproject core 

# Banco de dados 

O banco de dados utilizado é o PostegreSQL. 

A configuração para uso desse db está no arquivo settings.py
