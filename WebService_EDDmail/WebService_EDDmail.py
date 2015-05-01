import json
from flask import Flask, request

#IMPORTANDO LO NECESARIO PARA LAS LISTAS ENCABEZADO
import Estructuras.Lista_encabezados as listas_encabezados
#IMPORTANDO LO NECESARIO PARA LA MATRIZ
import Estructuras.Raiz_Matriz as raiz_matriz
import Estructuras.Raiz_listas as raiz_listas
import Estructuras.Matriz as matriz


app = Flask(__name__)

@app.route('/consultar_dominios',methods=['GET'])
def consultar_dominio():
    resultado = list_x.imprimir_eje_x()
    return json.dumps(resultado)

@app.route('/nuevo_usuario',methods=['POST'])
def nuevo_usuario():
    usuario = request.form['usuario']
    password = request.form['password']
    inicial = request.form['inicial']
    dominio = request.form['dominio']
    matrix.insertar_usuario_matriz(inicial,dominio,usuario,password)

@app.route('/buscar_usuario',methods=['POST'])
def buscar_usuario():
    usuario = request.form['usuario']
    inicial = request.form['inicial']
    dominio = request.form['dominio']
    #matrix.insertar_usuario_matriz(inicial,dominio,usuario)

@app.route('/dropbox/enviar_correo',methods =['POST'])
def recibir_correo():
    destinatario = request.form['destinatario']
    emisor =  request.form['emisor']
    mensaje = request.form['mensaje']
    return 'false'

if __name__ == '__main__':
    #SETENADO LAS LISTAS DE LOS ENCABEZADOS
    list_x = listas_encabezados.Lista_encabezado()
    list_y = listas_encabezados.Lista_encabezado()
    list_x.crear_x()
    list_y.crear_y()
    app.run(host='0.0.0.0')
