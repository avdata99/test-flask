from flask import Flask, render_template
from func.funciones import suma


# Crear una aplicacion Flask
app = Flask(
    __name__,
    # Carpeta donde se encuentran los archivos estáticos
    static_folder='static',
    # Carpeta donde se encuentran los templates para el frontend
    template_folder='templates'
)

@app.route('/')
def hello():
    site_title = 'Mi aplicacion web'
    return render_template("index.html", site_title=site_title)

@app.route('/sumar/<int:a>/<int:b>')
def flk_suma(a, b):
    return f'La suma es: {suma(a, b)}'
