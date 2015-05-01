__author__ = 'Cristian'

#IMPORTANDO LO NECESARIO PARA LA MATRIZ
import Estructuras.Lista_encabezados as listas
import Estructuras.Nodo_matriz as nodo_matriz
import Estructuras.Nodo_usuarios as nodo_usuario
#IMPORTANDO LO NECESSARIO PARA LA LISTA DE USUARIOS
import Estructuras.Lista_usuarios as lista_prof
#IMPÓRTANDO LO NECESARIO  PARA LA LISTA DE CATEGORIAS
import Estructuras.Lista_categorias as lista_cate
#IMPORTANDO LO NECESARIO PARA EL ARBOL DE LOS REMITENTES
import Estructuras.ArbolABB_remitente as arbol
#IMPORTANDO LO NECESARIO PARA LA LISTA DE CORREOS

class Matriz(object):
    #CONSTRUCTOR DE LA CLASE
    def __init__(self):
        #INCIIANDO LAS LISTAS CABECERAS
        self.list_x = listas.Lista_encabezado()
        self.list_y = listas.Lista_encabezado()
        #INICIANDO LA LISTA PARA LOS USUARIOS
        self.lista_prof = lista_prof.Lista_usuarios()
        #INICIANDO LA LISTA PARA LAS CATEGORIAS DE USARIOS
        self.lista_categorias = lista_cate.Lista_categorias()
        #INICIANDO EL ARBOL DE REMITENTES DE CORREOS
        self.arbol = arbol.ArbolABB()
    def es_vacia(self, raiz):
        if raiz.get_first() != None:
            return False
        else:
            return True
        return
    '''METODOS PARA LA INSERCCION DE NUEVOS USUARIOS EN LA MATRIZ, AQUI SE INSERTAN LAS NUEVAS CABECERAS EN X
    SI NO EXISTIERAN, EN CASO QUE EL NODO DE LA MATRIZ EXISTIERA SE INSERTA LA LISTA DE PROFUNDIDAD DE USUARIOS
    ESO SE MANEJA UNICAMENTE EN EL EJE X SE INSERTA CON SU LISTA DE CATEGORIA GENERAL POR DEFECTO LAS DEMAS
    ESTRUCTURAS SE INSERTAN CONFORME LAS NECESIDADES EL USUARIO'''
    def insertar_usuario_matriz(self,cabecera_x,cabecera_y,usuario, password):
        '''SE CREA UN  NODO DEL TIPO MATRIZ QUE SERA EL QUE CONTENGA TODA LA INFORMACION DE ESA
        ***SECCION DE LA MATRIZ, CABECERAS, ESTRUCTURAS
        ***SE CREA UN NODO DEL TIPO USUARIO QUE CONTENDRA LA INOFRMACION DEL USUARIO Y DENTRO SUS ESTRUCTURAS'''
        nuevo_nodo = nodo_matriz.Nodo_Matriz(cabecera_x, cabecera_y)
        nuevo_usuario = nodo_usuario.Nodo_matriz(usuario,password)
        self.lista_categorias.insertar(nuevo_usuario.get_root_seccion(),'General')
        encabezado_x = self.list_x.buscar(cabecera_x)
        encabezado_y = self.list_y.buscar(cabecera_y)
        if encabezado_x != None:
            self.insertar_matriz_x(encabezado_x,encabezado_y, nuevo_usuario, nuevo_nodo)
            self.insertar_matriz_y(encabezado_x,encabezado_y, nuevo_usuario, nuevo_nodo)
        else:
            self.list_x.insertar(cabecera_x)
            encabezado_x = self.list_x.buscar(cabecera_x)
            self.insertar_matriz_x(encabezado_x,encabezado_y, nuevo_usuario, nuevo_nodo)
            self.insertar_matriz_y(encabezado_x,encabezado_y, nuevo_usuario, nuevo_nodo)

    #MANEJO DE LA INSERCCION EN EL EJE X
    #ESTE METODO MANEJARA LA INSERCCION DE NUEVOS USUARIOS UNICAMENTE, YA QUE ASI NO SE
    #AGREGARAN DUPLICADOS Y SE MANEJARA LA PROFUNDIDAD CON MAYOR EXACTITUD
    def insertar_usuario_matriz_x(self,encabezado_x, nuevo_nodo, nuevo_usuario):
        #Inserccion en el eje x de la matrix
        if encabezado_x.get_first() != None:
            if(encabezado_x.get_first().get_y() > nuevo_nodo.get_y()):
                self.insertar_inicio(encabezado_x,nuevo_usuario)
            elif(encabezado_x.get_last().get_y() < nuevo_nodo.get_y()):
                self.insertar_final(encabezado_x,nuevo_usuario)
            else:#SE INSERTARA EN UNA DE LAS POSICIONES ENTRE LA PRIMERA Y ULITMA
                self.insertar_centro_x(encabezado_x,nuevo_nodo,nuevo_usuario)
        else:
            encabezado_x.set_first(nuevo_nodo)
            encabezado_x.set_last(nuevo_nodo)
            #SE INSERTA EL NUEVO USUARIO DENTRO DEL NODO DE LA RAIZ EN FORMA DE LISTA
            self.lista_prof.insertar(nuevo_nodo.get_root_users(),nuevo_usuario)
    def insertar_inicio_x(self,encabezado_x, nuevo_nodo,nuevo_usuario):
        nuevo_nodo.set_down(encabezado_x.get_first())
        encabezado_x.get_first().set_up(nuevo_nodo)
        encabezado_x.set_first(nuevo_nodo)
        self.lista_prof(nuevo_nodo.get_root_users(),nuevo_usuario)
    def insertar_centro_x(self,encabezado_x, nuevo_nodo, nuevo_usuario):
        aux = encabezado_x.get_first()#SE POSICIONA AL INICIO DE LOS ENCABEZADOS
        while aux != None:#MIENTRAS LA LISTA DE ENCABEZADOS NO ESTE VACIA
            if aux.get_y() > nuevo_nodo.get_y():
                aux = aux.get_down()
            elif aux.get_y == nuevo_nodo.get_y():#SI LOS DATOS COINCIDEN
                self.insertar_profundidad(aux,nuevo_usuario)#SE INSERTA SOLO EL NODO DE USUARIO EN EL NODO MATRIZ ACTUAL
                break#EL NUEVO SE OMITE PUES NO ES NECESARIO SOBREESCRIBIR EL NODO ANTERIOR
            else:
                nuevo_nodo.set_up(aux.get_up())
                nuevo_nodo.set_down(aux)
                aux.get_up().set_down(nuevo_nodo)
                aux.set_up(nuevo_nodo)
                break
    def insertar_final_x(self,encabezado_x,nuevo_nodo,nuevo_usuario):
        nuevo_nodo.set_up(encabezado_x.get_last())
        encabezado_x.get_last().set_down(nuevo_nodo)
        encabezado_x.set_last(nuevo_nodo)
        self.lista_prof.insertar(nuevo_nodo.get_root_users(),nuevo_usuario)

    #MANEJO DE LA INSERCCION EN EL EJE Y ACA NO SE MANEJA LA PROFUNDIDAD
    #TAMPOCO SE MANEJAN LAS INSERCCIONES DE NUEVOS USUARIOS
    #SOLAMENTE SE ENLAZA EL NUEVO NODO CON ESTE EJE
    def insertar_usuario_matriz_y(self,encabezado_y,nuevo_nodo,nuevo_usuario):
        #Inserccion en el eje y de la matrix
        if encabezado_y.get_first() != None:
            if(encabezado_y.get_first().get_x() > nuevo_nodo.get_x()):
                self.insertar_inicio(encabezado_y,nuevo_usuario)
            elif(encabezado_y.get_last().get_x() < nuevo_nodo.get_x()):
                self.insertar_final(encabezado_y,nuevo_usuario)
            else:
                self.insertar_centro_y(encabezado_y,nuevo_usuario)
        else:
            encabezado_y.set_first(nuevo_nodo)
            encabezado_y.set_last(nuevo_nodo)
    def insertar_inicio_y(self,encabezado, nuevo_nodo):
        nuevo_nodo.set_next(encabezado.get_first())
        encabezado.get_first().set_back(nuevo_nodo)
        encabezado.set_first(nuevo_nodo)
    def insertar_centro_y(self,encabezado_y, nuevo_nodo):
        aux = encabezado_y.get_first()
        while aux != None:
            if aux.get_y() > nuevo_nodo.get_y():
                aux = aux.get_next()
            else:
                nuevo_nodo.set_back(aux.get_back())
                nuevo_nodo.set_next(aux)
                aux.get_back().set_next(nuevo_nodo)
                aux.set_back(nuevo_nodo)
                break
    def insertar_final_y(self,encabezado,nuevo_nodo):
        nuevo_nodo.set_back(encabezado.get_last())
        encabezado.get_last().set_next(nuevo_nodo)
        encabezado.set_last(nuevo_nodo)
    #MANEJO DE LA INSERCCION EN PROFUNDIDAD DE LA ESTRUCTURA
    def insertar_profundidad(self,nodo_atual, nuevo_usuario):
        self.lista_prof.insertar(nodo_atual.get_root_users(), nuevo_usuario)
    '''********************************METODOS PARA LA BUSQUEDA******************************************************'''
    def buscar_nodo_matriz(self,cabecera_x,cabecera_y):
        encabezado_y = self.list_y.buscar(cabecera_y)
        encontrado = None
        aux = None
        if encabezado_y.get_first() != None:
            aux = encabezado_y.get_first()
            while aux != None:
                if aux.get_x() != cabecera_x:
                    aux = aux.get_next()
                else:
                    encontrado = aux
                    break
        return encontrado
    def buscar_usuario_matriz(self,nodo_matriz,usuario):
        encontrado = None
        encontrado = self.lista_usuarios.buscar_usuario(nodo_matriz.get_root_users(),usuario)
        return encontrado
    def buscar_categoria_usuario(self,usuario,categoria):
        encontrado = None
        encontrado = self.lista_categorias.buscar_categoria(usuario.get_root_seccion(),categoria)
        return encontrado
    def buscar_remitente_usuario(self,categoria,remitente):
        encontrado = None
        encontrado = self.arbol.buscar(categoria.get_root_mail(),remitente)
        return remitente
    def buscar_correo_usuario(self,remitente,msj):
        encontrado = None

    '''***************************METODOS PARA LA INSERCCION DE NUEVAS CATEGORIAS************************************'''
    '''***************************METODOS PARA LA INSERCCION DE NUEVOS REMITENTES************************************'''
    '''*****************************METODOS PARA LA INSERCCION DE NUEVOS USUARIOS************************************'''
    '''*****************************METODOS PARA LA IMPRESION DE LAS ESTRUCTURAS*************************************'''

pass