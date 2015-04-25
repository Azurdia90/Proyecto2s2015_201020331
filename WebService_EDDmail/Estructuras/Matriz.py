__author__ = 'Cristian'
import Estructuras.Lista_encabezado as listas
import Estructuras.Nodo_matriz as nodo
class Matriz(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, raiz_x, raiz_y):
        self.root_x = raiz_x
        self.root_y = raiz_y
        self.list_x = listas.Lista_encabezado(self.root_x)
        self.list_y = listas.Lista_encabezado(self.root_y)
    def es_vacia(self, raiz):
        if raiz.get_first() != None:
            return False
        else:
            return True
    #METODO QUE PERMITIRA INSERTAR UN NUEVO USUARIO EN LA MATRIZ, DE MANERA QUE ESTE USUARIO
    #CONTENDRA OTRAS ESTRUCTURAS EN SU INSERIOR, SI NO EXISTE EL ENCABEZADO EN EJE X SE CREA
    def insertar_usuario_matriz(self,cabecera_x,cabecera_y,usuario):
        nuevo_usuario = nodo.Nodo_matriz(usuario, cabecera_x, cabecera_y)
        encabezado_x = self.list_x.buscar(cabecera_x)
        encabezado_y = self.list_y.buscar(cabecera_y)
        if encabezado_x != None:
            self.insertar_matriz_x(encabezado_x,encabezado_y, nuevo_usuario)
            self.insertar_matriz_y(encabezado_x,encabezado_y, nuevo_usuario)
        else:
            self.list_x.insertar(cabecera_x)
            encabezado_x = self.list_x.buscar(cabecera_x)
            self.insertar_matriz_x(encabezado_x,encabezado_y, nuevo_usuario)
            self.insertar_matriz_y(encabezado_x,encabezado_y, nuevo_usuario)

    #MANEJO DE LA INSERCCION EN EL EJE X
     def insertar_usuario_matriz_x(self,encabezado_x, nuevo_usuario):
        #Inserccion en el eje x de la matrix
        if encabezado_x.get_first() != None:
            if(encabezado_x.get_first().get_y() > nuevo_usuario.get_y()):
                self.insertar_inicio(encabezado_x,nuevo_usuario)
            elif(encabezado_x.get_last().get_y() < nuevo_usuario.get_y()):
                self.insertar_final(encabezado_x,nuevo_usuario)
            else:
                self.insertar_centro_x(encabezado_x,nuevo_usuario)
        else:
            encabezado_x.set_first(nuevo_usuario)
            encabezado_x.set_last(nuevo_usuario)
    def insertar_inicio_x(self,encabezado_x, nuevo_usuario):
        nuevo_usuario.set_down(encabezado_x.get_first())
        encabezado_x.get_first().set_up(nuevo_usuario)
        encabezado_x.set_first(nuevo_usuario)
    def insertar_centro_x(self,encabezado_x, nuevo_usuario):
        aux = encabezado_x.get_first()
        while aux != None:
            if aux.get_y() > nuevo_usuario.get_y():
                aux = aux.get_down()
            elif aux.get_y == nuevo_usuario.get_y():
                self.insertar_profundidad(aux,nuevo_usuario)
                break
            else:
                nuevo_usuario.set_up(aux.get_up())
                nuevo_usuario.set_down(aux)
                aux.get_up().set_down(nuevo_usuario)
                aux.set_up(nuevo_usuario)
                break
    def insertar_final_x(self,encabezado_x,nuevo_usuario):
        nuevo_usuario.set_up(encabezado_x.get_last())
        encabezado_x.get_last().set_down(nuevo_usuario)
        encabezado_x.set_last(nuevo_usuario)

    #MANEJO DE LA INSERCCION EN EL EJE Y ACA NO SE MANEJA LA PROFUNDIDAD
    def insertar_usuario_matriz_y(self,encabezado_y, nuevo_usuario):
        #Inserccion en el eje y de la matrix
        if encabezado_y.get_first() != None:
            if(encabezado_y.get_first().get_x() > nuevo_usuario.get_x()):
                self.insertar_inicio(encabezado_y,nuevo_usuario)
            elif(encabezado_y.get_last().get_x() < nuevo_usuario.get_x()):
                self.insertar_final(encabezado_y,nuevo_usuario)
            else:
                self.insertar_centro_y(encabezado_y,nuevo_usuario)
        else:
            encabezado_y.set_first(nuevo_usuario)
            encabezado_y.set_last(nuevo_usuario)
    def insertar_inicio_y(self,encabezado, nuevo_usuario):
        nuevo_usuario.set_next(encabezado.get_first())
        encabezado.get_first().set_back(nuevo_usuario)
        encabezado.set_first(nuevo_usuario)
    def insertar_centro_y(self,encabezado_y, nuevo_usuario):
    def insertar_final_y(self,encabezado,nuevo_usuario):
        nuevo_usuario.set_back(encabezado.get_last())
        encabezado.get_last().set_next(nuevo_usuario)
        encabezado.set_last(nuevo_usuario)
    #MANEJO DE LA INSERCCION EN PROFUNDIDAD DE LA ESTRUCTURA
    def insertar_profundidad(self,usuario_actual, nuevo_usuario):
        if usuario_actual.get_previous() != None
        else:
            usuario_actual


pass