__author__ = 'Cristian'

class Lista_usuarios(object):

    def es_vacia(self, root):
        if root.get_first() == None:
            return True
        else:
            return False
    def insertar(self, root, nuevo):
        if self.es_vacia(root) == False:
            if(root.get_first().get_user()>nuevo.get_user()):
                #INSERTAR AL INICIO
                self.insertar_inicio(root,nuevo)
            elif(root.get_last().get_user()<nuevo.get_user()):
                #INSERTAR AL FINAL
                self.insertar_final(root,nuevo)
            else:
                #INSERTAR EN UNA POSICION ESPECIFICA
                self.insertar_centro(root,nuevo)
        else:
            root.set_first(nuevo)
            root.set_last(nuevo)
    #METODOS DE INSERCCION EN LISTA ENLAZADA
    def insertar_inicio(self,root, nuevo):
        nuevo.set_next(root.get_first())
        root.get_first().set_back(nuevo)
        root.set_first(nuevo)

    def insertar_centro(self,root,nuevo):
        aux = root.get_first()
        while(aux != None):
            if(aux.get_user()< nuevo.get_user()):
                aux = aux.get_next()
            elif aux.get_user() == nuevo.get_user():
                break
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
    def buscar_usuario(self,root,usuario,password):
        if self.es_vacia(root) == False:
            aux = root.get_first()
            while aux != None:
                if aux.get_user() != usuario and aux.get_pass() != password:
                    aux = aux.get_next()
                else:
                    return  aux
def lista_usuarios(self,root):
        grafica = None
        grafica = 'digraph usuarios{ \n'
        if self.es_vacia(root) != True:
            aux = root.get_first()
            while(aux != None):
                grafica += 'nodo'+aux.get_user()+'[shape=box,label="'+aux.get_user()+'"];\n'
                if(aux.get_next!=None):
                    grafica += 'nodo'+aux.get_user()+'->nodo'+aux.get_next().get_user()+';\n'
                if(aux.get_back!=None):
                    grafica += 'nodo'+aux.get_user()+'->nodo'+aux.get_back().get_user()+';\n'
                aux = aux.get_next()
        else:
            grafica += 'lista_vacia[shape=box,label="Lista Vacia"];\n'
        grafica += '}'
        return grafica
pass
