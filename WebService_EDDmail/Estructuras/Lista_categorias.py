__author__ = 'Cristian'

class Lista_categorias(object):

    def es_vacia(self, root):
        if root.get_first() == None:
            return True
        else:
            return False
    def insertar(self, root, nuevo):
        if self.es_vacia(root) != True:
            if(root.get_first().get_seccion()>nuevo.get_seccion()):
                #INSERTAR AL INICIO
                self.insertar_inicio(root,nuevo)
            elif(root.get_last().get_seccion()<nuevo.get_seccion()):
                #INSERTAR AL FINAL
                self.insertar_final(root,nuevo)
            else:
                #INSERTAR EN UNA POSICION ESPECIFICA
                self.insertar_centro(root,nuevo)
        else:
            self.root.set_first(nuevo)
            self.root.set_last(nuevo)
    #METODOS DE INSERCCION EN LISTA ENLAZADA
    def insertar_inicio(self,root, nuevo):
        nuevo.set_next(root.get_first())
        root.get_first().set_back(nuevo)
        root.set_first(nuevo)

    def insertar_centro(self,root,nuevo):
        aux = root.get_first()
        while(aux != None):
            if(aux.get_seccion()> nuevo.get_seccion()):
                aux = aux.get_next()
            else:
                nuevo.set_back(aux.get_back())
                nuevo.set_next(aux)
                aux.get_back().set_next(nuevo)
                aux.set_back(nuevo)
                break
    def insertar_final(self,root,nuevo):
        nuevo.set_back(root.get_last())
        root.get_last().set_next(nuevo)
        root.set_last(nuevo)
    def buscar_categoria(self,root,categoria):
        encontrado = None
        aux = None
        if self.es_vacia(root) != True:
            aux = root.get_first()
            while aux != None:
                if aux.get_seccion() != categoria:
                    aux = aux.get_next()
                else:
                    encontrado = aux
                    break
        return encontrado
pass