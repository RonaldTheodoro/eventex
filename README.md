# Eventex

Sistema de eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/RonaldTheodoro/eventex.svg?branch=master)](https://travis-ci.org/RonaldTheodoro/eventex)

## Como desenvolver?

1) Clone o repositorio
2) Crie um virtualenv com Python 3.5
3) Ative o virtualenv
4) Instale as dependeincias
5) Configure a instancia com o .env
6) Execute os testes

```console

git clone https://github.com/RonaldTheodoro/eventex.git wttd
cd wttd
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test

```

## Como fazer o deploy?

1) Crie um instancia no heroku
2) Envie as configurações para o heroku
3) Defina uma SECRET_KEY para a instancia
4) Defina DEBUG=False
5) Configure o serviço de email
6) Envie o codigo para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configurar o email
git push heroku master --force
```
