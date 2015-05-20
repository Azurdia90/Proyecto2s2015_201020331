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
    def __init__(self,listx,listy):
        #INCIIANDO LAS LISTAS CABECERAS
        self.list_x = listx
        self.list_y = listy
        #INICIANDO LA LISTA PARA LOS USUARIOS
        self.lista_profundidad = lista_prof.Lista_usuarios()
        #INICIANDO LA LISTA PARA LAS CATEGORIAS DE USARIOS
        self.lista_categorias = lista_cate.Lista_categorias()
        #INICIANDO EL ARBOL DE REMITENTES DE CORREOS
        self.arbol = arbol.ArbolABB()
        #INICIANDO EL STRING DE GRAFICA DEL .DOT
        self.grafica = ''
    '''METODOS PARA PODER ACTUALIZAR LA LISTA DE LOS ENCABEZADOS EN CASO DE SER MODIFICADOS'''
    def get_list_x(self):
        return self.list_x
    def set_list_x(self, listx):
        self.list_x = listx
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
    def insertar_usuario_matriz(self,cabecera_x,cabecera_y,usuario,password):
        '''SE CREA UN  NODO DEL TIPO MATRIZ QUE SERA EL QUE CONTENGA TODA LA INFORMACION DE ESA
        ***SECCION DE LA MATRIZ, CABECERAS, ESTRUCTURAS
        ***SE CREA UN NODO DEL TIPO USUARIO QUE CONTENDRA LA INOFRMACION DEL USUARIO Y DENTRO SUS ESTRUCTURAS'''
        nuevo_nodo = nodo_matriz.Nodo_matriz(cabecera_x,cabecera_y)
        nuevo_usuario = nodo_usuario.Nodo_usuario(usuario,password)
        self.lista_categorias.insertar(nuevo_usuario.get_root_seccion(),'General')
        encabezado_x = self.list_x.buscar(cabecera_x)
        encabezado_y = self.list_y.buscar(cabecera_y)
        if encabezado_x != None:
            self.insertar_eje_x(encabezado_x,nuevo_nodo,nuevo_usuario)
            self.insertar_eje_y(encabezado_y,nuevo_nodo)
        else:
            self.list_x.insertar(cabecera_x)
            encabezado_2 = self.list_x.buscar(cabecera_x)
            self.insertar_eje_x(encabezado_2,nuevo_nodo,nuevo_usuario)
            self.insertar_eje_y(encabezado_y,nuevo_nodo)

    #MANEJO DE LA INSERCCION EN EL EJE X
    #ESTE METODO MANEJARA LA INSERCCION DE NUEVOS USUARIOS UNICAMENTE, YA QUE ASI NO SE
    #AGREGARAN DUPLICADOS Y SE MANEJARA LA PROFUNDIDAD CON MAYOR EXACTITUD
    def insertar_eje_x(self,encabezado_x,nuevo_nodo,nuevo_usuario):
        #Inserccion en el eje x de la matrix
        if encabezado_x.get_first() != None:
            if(encabezado_x.get_first().get_y() > nuevo_nodo.get_y()):
                self.insertar_inicio_x(encabezado_x,nuevo_nodo,nuevo_usuario)
            elif(encabezado_x.get_last().get_y() < nuevo_nodo.get_y()):
                self.insertar_final_x(encabezado_x,nuevo_nodo,nuevo_usuario)
            else:#SE INSERTARA EN UNA DE LAS POSICIONES ENTRE LA PRIMERA Y ULITMA
                self.insertar_centro_x(encabezado_x,nuevo_nodo,nuevo_usuario)
        else:
            encabezado_x.set_first(nuevo_nodo)
            encabezado_x.set_last(nuevo_nodo)
            self.lista_profundidad.insertar(nuevo_nodo.get_root_users(),nuevo_usuario)#SE INSERTA EL NUEVO USUARIO DENTRO DEL NODO DE LA RAIZ EN FORMA DE LISTA
    def insertar_inicio_x(self,encabezado_x, nuevo_nodo,nuevo_usuario):
        nuevo_nodo.set_down(encabezado_x.get_first())
        encabezado_x.get_first().set_up(nuevo_nodo)
        encabezado_x.set_first(nuevo_nodo)
        self.lista_profundidad.insertar(nuevo_nodo.get_root_users(),nuevo_usuario)
    def insertar_centro_x(self,encabezado_x, nuevo_nodo, nuevo_usuario):
        aux = encabezado_x.get_first()#SE POSICIONA AL INICIO DE LOS ENCABEZADOS
        while aux != None:#MIENTRAS LA LISTA DE ENCABEZADOS NO ESTE VACIA
            if aux.get_y() < nuevo_nodo.get_y():
                aux = aux.get_down()
            elif aux.get_y() == nuevo_nodo.get_y():#SI LOS DATOS COINCIDEN
                self.insertar_profundidad(aux,nuevo_usuario)#SE INSERTA SOLO EL NODO DE USUARIO EN EL NODO MATRIZ ACTUAL
                break#EL NUEVO SE OMITE PUES NO ES NECESARIO SOBREESCRIBIR EL NODO ANTERIOR
            else:
                nuevo_nodo.set_up(aux.get_up())
                nuevo_nodo.set_down(aux)
                aux.get_up().set_down(nuevo_nodo)
                aux.set_up(nuevo_nodo)
                self.lista_profundidad.insertar(nuevo_nodo.get_root_users(),nuevo_usuario)
                break
    def insertar_final_x(self,encabezado_x,nuevo_nodo,nuevo_usuario):
        nuevo_nodo.set_up(encabezado_x.get_last())
        encabezado_x.get_last().set_down(nuevo_nodo)
        encabezado_x.set_last(nuevo_nodo)
        self.lista_profundidad.insertar(nuevo_nodo.get_root_users(),nuevo_usuario)

    #MANEJO DE LA INSERCCION EN EL EJE Y ACA NO SE MANEJA LA PROFUNDIDAD
    #TAMPOCO SE MANEJAN LAS INSERCCIONES DE NUEVOS USUARIOS
    #SOLAMENTE SE ENLAZA EL NUEVO NODO CON ESTE EJE
    def insertar_eje_y(self,encabezado_y,nuevo_nodo):
        #Inserccion en el eje y de la matrix
        if encabezado_y.get_first() != None:
            if(encabezado_y.get_first().get_x() > nuevo_nodo.get_x()):
                self.insertar_inicio_y(encabezado_y,nuevo_nodo)
            elif(encabezado_y.get_last().get_x() < nuevo_nodo.get_x()):
                self.insertar_final_y(encabezado_y,nuevo_nodo)
            else:
                self.insertar_centro_y(encabezado_y,nuevo_nodo)
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
            if aux.get_x() < nuevo_nodo.get_x():
                aux = aux.get_next()
            if aux.get_x() == nuevo_nodo.get_x():
                break
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
        self.lista_profundidad.insertar(nodo_atual.get_root_users(), nuevo_usuario)
    '''************************************METODOS PARA LA INSERCCION DE NUEVAS CATEGORIAS***************************'''
    def insertar_categoria(self,raiz, categoria):
        self.lista_categorias.insertar(raiz,categoria)
    '''********************************METODOS PARA LA BUSQUEDA******************************************************'''
    def buscar_nodo_matriz(self,cabecera_x,cabecera_y):
        encabezado_y = self.list_y.buscar(cabecera_y)
        aux = None
        if encabezado_y.get_first() != None:
            aux = encabezado_y.get_first()
            while aux != None:
                if aux.get_x() != cabecera_x:
                    aux = aux.get_next()
                else:
                    return  aux
    def buscar_usuario_matriz(self,raiz,usuario,password):
        encontrado = None
        encontrado = self.lista_profundidad.buscar_usuario(raiz,usuario,password)
        return encontrado
    def buscar_remitente_usuario(self,categoria,remitente):
        encontrado = None
        encontrado = self.arbol.buscar(categoria.get_root_mail(),remitente)
        return remitente
    def buscar_correo_usuario(self,remitente,msj):
        encontrado = None
    #IMPRIMIENDO ESTRUCTURAS COMPLETAS
    def buscar_lista_categorias(self,usuario):
        encontrado = None
        encontrado = self.lista_categorias.json_categorias(usuario)
        return encontrado

    '''***************************METODOS PARA LA INSERCCION DE NUEVAS CATEGORIAS************************************'''
    '''***************************METODOS PARA LA INSERCCION DE NUEVOS REMITENTES************************************'''
    '''*****************************METODOS PARA LA INSERCCION DE NUEVOS USUARIOS************************************'''
    '''*****************************METODOS PARA LA IMPRESION DE LAS ESTRUCTURAS*************************************'''
    def imprimir_matriz(self):
        self.grafica = 'digraph Matriz { \n'
        self.grafica += 'raiz_matriz [shape = box, label=\"EDD_MAIL \"]; \n'
        if self.list_x.get_raiz_lista().get_first() != None:
            self.grafica += 'raiz_matriz->"x_'+self.list_x.get_raiz_lista().get_first().get_encabezado()+'"[constraint=false];\n'
            self.grafica += self.list_x.graficar_x()
        if self.list_y.get_raiz_lista().get_first() != None:
            self.grafica += 'raiz_matriz->y_'+self.list_y.get_raiz_lista().get_first().get_encabezado()+';\n'
            self.grafica += self.list_y.graficar_y()
        self.grafica += '\n}'
        return self.grafica
    def imprimir_categorias(self,usuario):
        grafica = self.lista_categorias.graficar_categorias(usuario.get_root_seccion())
        return grafica
pass