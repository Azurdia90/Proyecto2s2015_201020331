import json
from flask import Flask, request
import Estructuras.Raiz_Matriz as raiz_matriz
import Estructuras.Raiz_encabezados as raiz_encabezado
import Estructuras.Lista_encabezado as lista_encabezado

app = Flask(__name__)

@app.route('/nuevo_usuario')
def nuevo_usuario():
    usuario = request.form['usuario']
    dominio = request.form['dominio']


if __name__ == '__main__':
    root_x = raiz_encabezado.Raiz_encabezado()
    root_y = raiz_encabezado.Raiz_encabezado()
    root_matrix = raiz_matriz.Raiz_Matriz()
    root_matrix.set_raiz_x(root_x)
    root_matrix.set_raiz_y(root_y)
    lista_x = lista_encabezado.Lista_encabezado(root_matrix.get_raiz_x())
    lista_y = lista_encabezado.Lista_encabezado(root_matrix.get_raiz_y())
    lista_y.crear_y()
    app.run()
