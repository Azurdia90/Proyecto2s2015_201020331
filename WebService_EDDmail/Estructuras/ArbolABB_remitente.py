__author__ = 'Cristian'
import Estructuras.Nodo_remitente as nodo
class ArbolABB(object):

    def __init__(self):
        self.root = None
        self.codigo = None

    def setear_codigo(self):
        self.codigo = None
    def es_vacia(self,root):
        if root != None:
            return False
        else:
            return True
    def insertar(self,root,remitente):
        retornar = None
        if self.es_vacia(root) !=  True:
            if root.get_remitente() < remitente:
                retornar = self.insertar(root.get_sub_derecho(),remitente)
            if root.get_remitente()> remitente:
                retornar = self.insertar(root.get_sub_izquierdo(),remitente)
        else:
            root = nodo.Nodo_ArbolABB(remitente)
            retornar = root
        return retornar
    def buscar(self,root,remitente):
        retornar = None
        if self.es_vacia(root) != True:
            if root.get_remitente() < remitente:
                retornar = self.buscar(root.get_sub_derecho(),remitente)
            if root.get_remitente() > remitente:
                retornar = self.buscar(root.get_sub_izquierdo(),remitente)
            if root.get_remitente() == remitente:
                retornar = root
        return retornar

    def imprimir(self,root):
        if self.es_vacia(root) == False:
            self.graficar_arbol(root.get_hijo_izquierdo())
            self.codigo = self.codigo + 'nodo'+root.get_remitente()+'[shape=ellipse, label="'+root.get_remitente()+'"];\n'
            if root.get_hijo_izquierdo() != None:
                self.codigo = self.codigo +'nodo'+root.get_remitente()+'->nodo'+root.get_hijo_izquierdo().get_iden()+';\n'
            if root.get_hijo_derecho() != None:
                self.codigo = self.codigo+'nodo'+root.get_iden()+'->nodo'+root.get_hijo_derecho().get_iden()+';\n'
            self.graficar_arbol(root.get_hijo_derecho())
        return self.codigo
