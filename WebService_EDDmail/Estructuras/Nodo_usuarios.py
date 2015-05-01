__author__ = 'Cristian'

import Estructuras.Raiz_listas as raiz_usuarios

class Nodo_matriz(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self,usuario,password):
        #DATOS DE REFERENCIA PARA LA INSERCCION
        self.usuario = usuario
        self.password = password
        self.next = None
        self.back = None
        #RAICES DE LAS ESTRUCTURAS ADICIONALES
        self.root_seccion = raiz_usuarios.Raiz_encabezado()
    #METODOS GET DE LA CLASE
    def get_user(self):
        return self.usuario
    def get_pass(self):
        return self.password
    def get_next(self):
        return self.next
    def get_back(self):
        return self.back
    def get_root_seccion(self):
        return self.root_seccion
    #METODOS SET DE LA CLASE
    def set_user(self,usuario):
        self.root_users = usuario
    def set_pass(self,password):
        self.password = password
    def set_next(self,next):
        self.next = next
    def set_back(self, back):
        self.back = back
    def set_root_seccion(self,usuarios):
        self.root_users = usuarios
pass