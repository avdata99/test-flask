from flask import Flask
from func.funciones import suma


# Crear una aplicacion Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hola <b>usuario!</b>'

@app.route('/sumar/<int:a>/<int:b>')
def flk_suma(a, b):
    return f'La suma es: {suma(a, b)}'
