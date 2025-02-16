PARA ACESSAR O AMBIENTE VIRTUAL 

source venv/Scripts/activate .

PARA CHAMAR O CODIGO

python app.py

PARA CRIAR O AMBIENTE VIRTUAL

python -m venv venv


COMO SUBIR O SERVIDOR NA SUA MAQUINA LOCAL USANDO UVICORN (FASTAPI)

uvicorn main:app --reload

control C  (encerra)

URLs para acesso do SERVIDOR

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/api/restaurantes/

ESPECIFICO
http://127.0.0.1:8000/api/restaurantes/?restaurante=KFC