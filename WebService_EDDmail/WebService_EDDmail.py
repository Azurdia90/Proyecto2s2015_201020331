import json
import requests
from flask import Flask, request

#IMPORTANDO LO NECESARIO PARA LAS LISTAS ENCABEZADO
import Estructuras.Lista_encabezados as listas_encabezados
#IMPORTANDO LO NECESARIO PARA LA MATRIZ
import Estructuras.Matriz as matriz


app = Flask(__name__)
'''**********************************METODOS PARA EL MANEJO DE LA MATRIZ*********************************************'''
@app.route('/consultar_dominios',methods=['GET'])
def consultar_dominio():
    resultado = list_x.imprimir_eje_x()
    return json.dumps(resultado)

@app.route('/nuevo_usuario',methods=['POST'])
def nuevo_usuario():
    objeto_json = request.json
    diccionario = objeto_json
    usuario = diccionario['usuario']
    password = diccionario['password']
    respuesta = {'mensaje':'Usuario Creado'}
    cabecera_y = usuario[0]
    cabecera_aux = usuario.split('@')
    cabecera_x = '@'+cabecera_aux[1]
    matrix.insertar_usuario_matriz(cabecera_x,cabecera_y,usuario,password)
    return json.dumps(respuesta)
@app.route('/buscar_usuario',methods=['POST'])
def buscar_usuario():
    objeto_json = request.json
    diccionario = objeto_json
    usuario = diccionario['usuario']
    password = diccionario['password']
    cabecera_y = usuario[0]
    cabecera_aux = usuario.split('@')
    cabecera_x = '@'+cabecera_aux[1]
    nodo = matrix.buscar_nodo_matriz(cabecera_x,cabecera_y)
    devolver = matrix.buscar_usuario_matriz(nodo.get_root_users(),usuario,password)
    respuesta = None
    if usuario != None:
        respuesta = {'usuario':devolver.get_user(),'password':devolver.get_pass()}
    else:
        respuesta = {'usuario':'¬','password':'¬'}
    return json.dumps(respuesta)
@app.route('/buscar_lista_categorias',methods=['POST'])
def buscar_lista_categorias():
    objeto_json = request.json
    diccionario = objeto_json
    usuario = diccionario['usuario']
    password = diccionario['password']
    cabecera_y = usuario[0]
    cabecera_aux = usuario.split('@')
    cabecera_x = '@'+cabecera_aux[1]
    nodo_matriz = matrix.buscar_nodo_matriz(cabecera_x,cabecera_y)
    nodo_usuario = matrix.buscar_usuario_matriz(nodo_matriz.get_root_users(),usuario,password)
    nodo_categoria = matrix.buscar_lista_categorias(nodo_usuario.get_root_seccion())
    resultado = {'categoria':nodo_categoria}
    return json.dumps(resultado)
@app.route('/insertar_categoria',methods=['POST'])
def insertar_categoria():
    objeto_json = request.json
    diccionario = objeto_json
    usuario = diccionario['usuario']
    password = diccionario['password']
    categoria = diccionario['categoria']
    cabecera_y = usuario[0]
    cabecera_aux = usuario.split('@')
    cabecera_x = '@'+cabecera_aux[1]
    nodo_matriz = matrix.buscar_nodo_matriz(cabecera_x,cabecera_y)
    nodo_usuario = matrix.buscar_usuario_matriz(nodo_matriz.get_root_users(),usuario,password)
    matrix.insertar_categoria(nodo_usuario.get_root_seccion(),categoria)
    respuesta = {'mensaje':'Categoria creada'}
    return json.dumps(respuesta)
'''********************************METODOS QUE SE MANEJARAN CON EL OTRO WEB SERVICE********************************'''
@app.route('/buscar',methods =['POST'])
def buscar():
    objeto_json = request.json
    dic = objeto_json
    usuario = dic['correo']
    password = dic['password']
    cabecera_y = usuario[0]
    cabecera_aux = usuario.split('@')
    cabecera_x = '@'+cabecera_aux[1]
    nodo_matriz = matrix.buscar_nodo_matriz(cabecera_x,cabecera_y)
    respuesta = ''
    if nodo_matriz != None:
        nodo_usuario = matrix.buscar_usuario_matriz(nodo_matriz.get_root_users(),usuario,password)
        if nodo_usuario != None:
            respuesta = {'Existe':'True'}
        else:
            respuesta = {'Existe':'False'}
    else:
        respuesta = {'Exite':'False'}
    return json.dumps(respuesta)
'''****************************METODOS PARA PODER GRAFICAR LAS ESTRUCTURAS QUE SE SOLICITAN**************************'''
@app.route('/graficar_matriz',methods=['GET'])
def graficar_matriz():
    grafica = matrix.imprimir_matriz()
    return grafica
@app.route('/graficar_lista_categorias',methods=['POST'])
def graficar_lista_categorias():
    objeto_json = request.json
    diccionario = objeto_json
    usuario = diccionario['usuario']
    password = diccionario['password']
    cabecera_y = usuario[0]
    cabecera_aux = usuario.split('@')
    cabecera_x = '@'+cabecera_aux[1]
    nodo_matriz = matrix.buscar_nodo_matriz(cabecera_x,cabecera_y)
    nodo_usuario = matrix.buscar_usuario_matriz(nodo_matriz.get_root_users(),usuario,password)
    grafica = matrix.imprimir_categorias(nodo_usuario)
    return grafica

'''*********************************************METODO PRINCIPAL DE FLASK********************************************'''
if __name__ == '__main__':
    #SETENADO LAS LISTAS DE LOS ENCABEZADOS
    list_x = listas_encabezados.Lista_encabezado()
    list_y = listas_encabezados.Lista_encabezado()
    list_x.crear_x()
    list_y.crear_y()
    matrix = matriz.Matriz(list_x,list_y)
    app.run(host='0.0.0.0', debug = True)
