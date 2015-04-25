__author__ = 'Cristian'

import Estructuras.Raiz_encabezados as raiz_seccion
class Nodo_usuarios(object):
    #METODO CONTRUCTOR DE LA CLASE
    def __init__(self):
        self.usuario
        self.root_seccion = raiz_seccion.Raiz_encabezado()
        self.root_mail = None
        self.next = None
        self.back = None
    #METODOS GET DE LA CLASE
    def get_usuario(self):
        return self.usuario()
    def get_root_seccion(self):
        return self.root_seccion
    def get_root_mail(self):
        return self.root_mail
    def get_next(self):
        return self.next
    def get_back(self):
        return self.back
    #METODOS SET DE LA CLASE
    def set_usuario(self,usuario):
        self.usuario = usuario
    def set_root_seccion(self,raiz):
        self.root_seccion = raiz
    def set_root_mail(self,raiz):
        self.root_mail=raiz
    def set_next(self,next):
        self.next=next
    def set_back(self,back):
        self.back = back