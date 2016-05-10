import webapp2
from google.appengine.ext import ndb
from Estructuras.Pasos import Paso
from Estructuras.Ingredientes import Ingrediente


class Receta(ndb.Model):

    # Id del usuario propietario de la receta
    id_usuario = ndb.GenericProperty()

    # Id de la categoria a la que pertenece la receta
    id_categoria = ndb.GenericProperty()

    # Nombre de la receta
    nombre = ndb.StringProperty()

    # Etiquetas de la receta
    etiquetas = ndb.StringProperty()

    # Clave para buscar la foto
    id_imagen = ndb.StringProperty()

    """
        Funcion para obtener directamente el id del objeto
    """
    def get_id(self):

        return self.key.id()

    """
        Funcion para insertar un paso a partir de una receta
    """
    def insertar_paso(self,desc,temp,pos):

        p = Paso(descripcion=desc,tiempo=temp,orden=pos,id_receta=self.get_id())
        p.put()

    """
        Funcion para insertar un paso a partir de una receta
    """

    def insertar_ingrediente(self, nombre, cantidad, descripcion):
        i = Ingrediente(nombre=nombre, cantidad=cantidad, descripcion=descripcion, id_receta=self.get_id())
        i.put()

    """
        Funcion para obtener los pasos de la receta en orden
    """
    def obtener_pasos(self):

        return Paso.query(Paso.id_receta==self.get_id()).order(Paso.orden)

    """
        Funcion para obtener los ingredientes de la receta
    """

    def obtener_ingredientes(self):
        return Ingrediente.query(Ingrediente.id_receta == self.get_id())
