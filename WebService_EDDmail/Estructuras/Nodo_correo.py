__author__ = 'Cristian'

class Nodo_correo(object):
    #METODO CONSTRUCTOR DE LA CLASE
    def __init__(self,msj):
        self.msj = msj
        self.next = None
        self.back = None
    #METODOS GET DE LA CLASE
    def get_msj(self):
        return self.msj
    def get_next(self):
        return self.next
    def get_back(self):
        return self.back
    #METODOS SET DE LA CLASE
    def set_msj(self,msj):
        self.msj = msj
    def set_next(self,next):
        self.next = next
    def set_back(self,back):
        self.back = back
pass