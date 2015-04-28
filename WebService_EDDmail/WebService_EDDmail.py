import json
from flask import Flask, request
import Estructuras.Raiz_Matriz as raiz_matriz
import Estructuras.Raiz_encabezados as raiz_encabezado
import Estructuras.Matriz as matriz

app = Flask(__name__)

@app.route('/nuevo_usuario')
def nuevo_usuario():
    usuario = request.form['usuario']
    password = request.form['password']
    inicial = request.form['inicial']
    dominio = request.form['dominio']
    matrix.insertar_usuario_matriz(inicial,dominio,usuario,password)

@app.route('/buscar_usuario')
def buscar_usuario():
    usuario = request.form['usuario']
    inicial = request.form['inicial']
    dominio = request.form['dominio']
    matrix.insertar_usuario_matriz(inicial,dominio,usuario,password)



if __name__ == '__main__':
    root_x = raiz_encabezado.Raiz_encabezado()
    root_y = raiz_encabezado.Raiz_encabezado()
    root_matrix = raiz_matriz.Raiz_Matriz()
    root_matrix.set_raiz_x(root_x)
    root_matrix.set_raiz_y(root_y)
    matrix = matriz.Matriz(root_matrix.get_raiz_x(),root_matrix.get_raiz_y())
    app.run()
