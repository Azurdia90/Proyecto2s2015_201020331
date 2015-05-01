__author__ = 'Cristian'
import Estructuras.Raiz_listas as raiz
import Estructuras.Nodo_encabezado as nodo

class Lista_encabezado(object):
    #METODO CONSTRUCTOR DE LA CLASE
    def __init__(self):
        self.root = raiz.Raiz_listas()
    #METODO PARA VERIFICAR SI LA ESTRUCTURA ESTA VACIA
    def es_vacia(self):
        if self.root.get_first() == None:
            return True
        else:
            return False
    #METODOS PARA DEVOLVER LA RAIZ
    def get_raiz_lista(self):
        return self.root
    def insertar(self,indice):
        nuevo = nodo.Nodo_encabezado(indice)
        if self.es_vacia() != True:
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
            if(aux.get_encabezado()< nuevo.get_encabezado()):
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
    def buscar(self,root,indice):
        aux = None
        if self.es_vacia() != True:
            aux = self.root.get_first()
            while(aux!=None):
                if(aux.get_encabezado() != indice):
                    aux = aux.get_next()
                else:
                    break
            return aux
        else:
            return aux
    '''********************************METODOS ESPECIFICOS DEL ENCABEZADO DEL EJE X*********************************'''
    #METODO PARA INICIAR EL EJE X DE LA MATRIZ
    def crear_x(self):
        self.insertar('@gmail.com')
        self.insertar('@hotmail.com')
        self.insertar('@outlook.com')
        self.insertar('@icloud.com')
        self.insertar('@yahoo.com')
    def imprimir_eje_x(self):
        resultado = []
        if self.es_vacia() != True:
            aux = self.root.get_first()
            while aux != None:
                resultado.append({'dominio':aux.get_encabezado()})
                aux = aux.get_next()
        else:
            resultado.append({'dominio':'La lista esta vacia'})
        return resultado
    '''********************************METODOS ESPECIFICOS DEL ENCABEZADO DEL EJE Y*********************************'''
    #METODO PARA INICIAR EL EJE Y DE LA MATRIZ
    def crear_y(self):
        for y in [97,122]:
            caracter = chr(y)
            self.insertar(caracter)
    #METODO DE GRAFICAR DEL EJE Y
    def graficar_y(self):
        grafica = None
        grafica = 'digraph Ejey { \n'
        if self.es_vacia() != True:
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
        return grafica
pass