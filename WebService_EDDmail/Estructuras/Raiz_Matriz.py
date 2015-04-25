__author__ = 'Cristian'

class Raiz_Matriz (object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self):
        self.Raiz_x = None #NODO CON QUE SE MANEJARA EL EJE X
        self.Raiz_y = None #NODO CON QUE SE MANEJARA EL EJE Y
    #METODOS GET DE LA RAIZ
    def get_raiz_x(self):
        return self.Raiz_x
    def get_raiz_y(self):
        return self.Raiz_y
    #METODOS SET DE LA RAIZ
    def set_raiz_x(self, raiz):
        self.Raiz_x = raiz
    def set_raiz_y(self, raiz):
        self.Raiz_y = raiz
pass #FIN DEL NODO RAIZ