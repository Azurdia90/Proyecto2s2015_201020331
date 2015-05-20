from flask import Flask, request, render_template, json
from arbolBCarpetas import BTree
from arbolAVLArchivos import AVLTree
from ListaDobleUsuarios import DoubleListUser
import requests
app = Flask(__name__)

miarbol = BTree(5)
archivos = AVLTree()
users = DoubleListUser()

@app.route('/')
def index():
    return render_template('hello.html', name='Estructuras De Datos')

@app.route('/carpetas', methods=['GET'])
def insert():
    miarbol= BTree(5)
    miarbol.insertar('test')
    miarbol.insertar('a')
    miarbol.insertar('hola')
    miarbol.insertar('edd')
    miarbol.insertar('Compi1')
    miarbol.insertar('instaladores')
    miarbol.insertar('fotos')
    # miarbol.insertar(14)
    # miarbol.insertar(15)
    # miarbol.insertar(16)
    # miarbol.insertar(18)
    # miarbol.insertar(19)
    # miarbol.insertar(20)
    # miarbol.insertar(21)
    # miarbol.insertar(30)
    # miarbol.insertar(35)
    # miarbol.insertar(39)
    # miarbol.insertar(46)
    # miarbol.insertar(56)
    # miarbol.insertar(66)
    # miarbol.insertar(70)
    # miarbol.insertar(71)
    # miarbol.insertar(72)
    # miarbol.insertar(75)
    # miarbol.insertar(81)
    # miarbol.insertar(82)

    res = miarbol.getDot()

    return str(res)

# Registro
@app.route('/registrarse')
def registrarse():
    return render_template('Registro.html')

@app.route('/registro_terminado', methods=['POST'])
def registro_terminado():
    correo=request.form['correo']
    password=request.form['password']
    #urlib
    url = 'http://192.168.0.18:5000/buscar'
    params = {'correo': correo, 'password': password}
    r = requests.post(url, json=params)
    print(r.content)
    #urlib
    res = users.append(correo, password)
    return render_template('RegistroTerminado.html', correo=correo, password=password, created=res)

# LogIn
#   Devuelve true si el usuario exite
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    correo=request.form['correo']
    password=request.form['password']
    res = users.dat(correo)
    if( res ):
        aux = users.buscar(correo)
        if(aux.contrasena == password):
            res = True
        else:
            res = False
    else:
        res = False
    return render_template('Login_validation.html', correo=correo, password=password, login=res)

# Usuarios
@app.route('/usuarios')
def showUsers():
    # res = users.show()
    res = users.getDot()
    print(res)
    return str(res)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        # port=int("5000"),
        debug=True
    )
