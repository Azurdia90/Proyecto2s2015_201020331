__author__ = 'Cristian'

import Estructuras.Raiz_encabezados as raiz_usuarios

class Nodo_matriz(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, x, y):
        #DATOS DE REFERENCIA PARA LA INSERCCION
        self.x = x
        self.y = y
        #PUNTEROS PARA LAS DOS DIMENSIONES DE LA MATRIZ
        self.next = None
        self.back = None
        self.up = None
        self.down = None
        #RAICES DE LA ESTRUCTURA DE PROFUNDIDAD
        self.root_users = raiz_usuarios.Raiz_encabezado()

    #METODOS GET DE LA CLASE
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_next(self):
        return self.next
    def get_back(self):
        return self.back
    def get_up(self):
        return self.up
    def get_down(self):
        return self.down
    def get_root_users(self):
        return self.root_users
    #METODOS SET DE LA CLASE
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_next(self,next):
        self.next = next
    def set_back(self, back):
        self.back = back
    def set_up(self, up):
        self.up = up
    def set_down (self,down):
        self.down = down
    def set_users(self,usuarios):
        self.root_users = usuarios
pass