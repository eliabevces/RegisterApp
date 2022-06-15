# RegisterApp
## Desafio CloulOpsS

### Configuração inicial

- Clonar o projeto

- [Instalar python](https://realpython.com/installing-python/) (caso for executar localmente)


- Instalar dependências (caso for executar localmente)
```bash
pip install requests==2.27.1 Django==4.0.5 django-cors-headers==3.13.0 djangorestframework==3.13.1 djongo==1.3.5 pymongo==3.12.3 python-dotenv==0.20.0 dnspython==2.2.1 django-bootstrap-form==3.4
```

- Criar o arquivo .env na raiz do projeto com as seguintes informações de acordo com o seu cluster mongoDB
```env
SECRET_KEY = <SECRET_KEY>
DB_DEFAULT_CLIENT_HOST = <MONGODB_CONNECTION_STRING>
DB_DEFAULT_CLIENT_NAME = <DATABASE_NAME>
```

## Executar projeto localmente

- Na pasta do repositório clonado execute comando:

```bash
python manage.py runserver
```

- Acesse o endereço http://127.0.0.1:8000

## Executar via docker

- Na pasta do repositório clonado execute comando:

```bash
docker build -t python-crud .
```

- Acesse o docker e adicione o arquivo .env

- Execute no docker o comando:
```bash
python manage.py runserver
```

- Acesse o endereço http://127.0.0.1:8000
