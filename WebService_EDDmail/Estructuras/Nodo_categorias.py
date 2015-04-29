__author__ = 'Cristian'

class Nodo_categorias(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self,categoria):
        self.seccion = categoria
        self.next = None
        self.back = None
        #RAICES DEL ARBOL DE LOS CORREOS
        self.root_mail = None
    #METODOS GET DE LA CLASE
    def get_seccion(self):
        return self.seccion
    def get_next(self):
        return self.next
    def get_back(self):
        return self.back
    def get_root_mail(self):
        return self.root_mail
    #METODOS SET DE LA CLASE
    def set_seccion(self,seccion):
        self.seccion = seccion
    def set_next(self,next):
        self.next = next
    def set_back(self,back):
        self.back = back
    def set_root_seccion(self,root):
        self.root_mail = root
pass