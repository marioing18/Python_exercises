#Documento que contiene las funciones de inserción, eliminación y actualización
#Designed by Abigail
#Se hará el uso de diccionarios para almacenar los productos y usuarios

class Empleado(object):
    
    def __init__(self, nombre, edad, direccion, telefono, correo, puesto, salario):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto
        self.salario = salario


    def __str__(self):

        print(f"""{self.nombre} tiene {self.edad}. 
        Vive en {self.direccion}
        Para contactarle, comuníquese al {self.telefono}
        o escriba a {self.correo}.
        Actualmente es nuestro/a {self.puesto}
        con un salario de {self.salario}$""")


class Producto(object):
    
    def __init__(self, nombre, id, cantidad, descrip, precio):
        self.nombre = nombre
        self.id = id
        self.cantidad = cantidad
        self.descrip = descrip
        self.precio = precio


    def __str__(self):

        print(f"""{self.nombre} es
              {self.descrip}.
              Actualmente tiene un precio sin rebajas de {self.precio}
              y están disponibles {self.cantidad} unidades.""")

    def __eq__(self, id):
        band = False
        try:

            if self.id == id:
                band = True
            else:
                band = False

        except TypeError:
            print("El id debe ser de tipo numérico, por favor corrige el registro")
        
        else:
            return band
        


class Registro(object):

    #Función para inicializar la clase
    def __init__(self,diccionario_de_valores):
        self.diccionario_de_valores = diccionario_de_valores
    
    #método asociado a la clase, para la inserción de valores
    def insercion(self, clave, valores):
        
        if clave not in self.diccionario_de_valores:

            self.diccionario_de_valores [clave] = valores


    def eliminación(self, clave):

         if clave in self.diccionario_de_valores:

            del self.diccionario_de_valores [clave]
    
    def actualización(self, clave, objeto):

         if clave in self.diccionario_de_valores:

            self.diccionario_de_valores [clave] = objeto
