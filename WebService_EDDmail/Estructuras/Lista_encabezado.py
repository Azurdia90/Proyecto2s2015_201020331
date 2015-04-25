__author__ = 'Cristian'

import Estructuras.Nodo_encabezado as nodo

class Lista_encabezado(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, raiz):
        self.root = raiz
    def es_vacia(self, raiz):
        if self.root.get_first() == None:
            return True
        else:
            return False
    #METODO INICIAL DE LA INSERCCION EN LA LISTA
    def crear_y(self):
        for y in [97,122]:
            caracter = chr(y)
            self.insertar(caracter)
    def insertar(self, indice):
        nuevo = nodo.Nodo_encabezado(indice)
        if self.es_vacia(self.root) != True:
            if(self.root.get_first().get_encabezado()>indice):
                #INSERTAR AL INICIO
                self.insertar_inicio(nuevo)
            elif(self.root.get_last().get_encabezado()<indice):
                #INSERTAR AL FINAL
                self.insertar_final(nuevo)
            else:
                #INSERTAR EN UNA POSICION ESPECIFICA
                self.insertar_centro(nuevo)
        else:
            self.root.set_first(nuevo)
            self.root.set_last(nuevo)
    #METODOS DE INSERCCION EN LISTA ENLAZADA
    def insertar_inicio(self,nuevo):
        nuevo.set_next(self.root.get_first())
        self.root.get_first().set_back(nuevo)
        self.root.set_first(nuevo)

    def insertar_centro(self,nuevo):
        aux = self.root.get_first()
        while(aux != None):
            if(aux.get_encabezado()> nuevo.get_encabezado()):
                aux = aux.get_next()
            else:
                nuevo.set_back(aux.get_back())
                nuevo.set_next(aux)
                aux.get_back().set_next(nuevo)
                aux.set_back(nuevo)
                break
    def insertar_final(self,nuevo):
        nuevo.set_back(self.root.get_last())
        self.root.get_last().set_next(nuevo)
        self.root.set_last(nuevo)
    def buscar(self,indice):
        aux = None
        if self.es_vacia(self.root) != True:
            aux = self.root.get_first()
            while(aux!=None):
                if(aux.get_encabezado() != indice):
                    aux = aux.get_next()
                else:
                    break
            return aux
        else:
            return aux
    #METODO DE IMPRESION DEL EJE Y
    def imprimir_y(self):
        grafica = None
        grafica = 'digraph Ejey { \n'
        if self.es_vacia(self.root) != True:
            aux = self.root.get_first()
            while(aux != None):
                grafica += 'nodo'+aux.get_encabezado()+'[shape=box,label="'+aux.get_encabezado()+'"];\n'
                if(aux.get_next!=None):
                    grafica += 'nodo'+aux.get_encabezado()+'->nodo'+aux.get_next().get_encabezado()+';\n'
                if(aux.get_back!=None):
                    grafica += 'nodo'+aux.get_encabezado()+'->nodo'+aux.get_back().get_encabezado()+';\n'
                aux = aux.get_next()
        else:
            grafica += 'lista_vacia[shape=box,label="Lista Vacia"];\n'
        grafica += '}'
pass