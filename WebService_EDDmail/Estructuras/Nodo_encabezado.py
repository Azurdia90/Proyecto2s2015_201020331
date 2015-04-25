__author__ = 'Cristian'

class Nodo_encabezado(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, encabezado):
        self.encabezado = encabezado
        self.first = None
        self.last = None
        self.next = None
        self.back = None
    #METODOS GET DE LA CLASE
    def get_encabezado(self):
        return self.encabezado
    def get_next(self):
        return self.next
    def get_back(self):
        return self.back
    #METODOS SET DE LA CLASE
    def set_encabezado(self,encabezado):
        self.encabezado = encabezado
    def set_next(self, next):
        self.next = next
    def set_back(self, back):
        self.back = back
pass  #FIN DE LA CLASE NODO ENCABEZADO