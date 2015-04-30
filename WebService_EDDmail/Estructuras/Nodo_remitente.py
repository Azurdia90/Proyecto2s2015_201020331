__author__ = 'Cristian'

import Estructuras.Raiz_encabezados as raiz

class Nodo_ArbolABB(object):
    def __init__(self, remitente,mensaje):
        self.remitente = remitente
        self.root_msj = raiz.Raiz_encabezado()
        self.sub_derecho = None
        self.sub_izquierdo = None
    def get_remitente(self):
        return self.remitente
    def get_root_msj(self):
        return self.root_msj
    def get_sub_derecho(self):
        return self.sub_derecho
    def get_sub_izquierdo(self):
        return self.sub_izquierdo
    def set_remitente(self,remitente):
        self.remitente = remitente
    def set_root_msj(self,msj):
        self.root_msj = msj
    def set_sub_derecho(self,derecho):
        self.sub_derecho = derecho
    def set_sub_izquierdo(self,izquierdo):
        self.sub_izquierdo = izquierdo
pass