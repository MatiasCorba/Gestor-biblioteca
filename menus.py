def validar_opcion(opcion,opciones):
    while True:
        try:
            if opcion in opciones:
               opcion
               return opcion
      
            print("Por favor seleccione el numero de la accion que desea realizar")
        except ValueError:
            print("Por favor seleccione el numero de la accion que desea realizar")

def menu_libros():

   opcion=int(input(" 1. Añadir libro\n 2. Eliminar libro\n 3. Buscar libros\n 4. Volver al menu anteriror\nQue desea hacer: "))
   gestion_libro=validar_opcion(opcion,{1,2,3,4})
   return gestion_libro

def menu_busqueda():
   opcion=int(input(" 1. Añadir usuario\n 2. Eliminar usuario\n 3. Buscar usuarios\n 4. Volver al menu anteriror\nQue desea hacer: "))
   gestion_busqueda=validar_opcion(opcion,{1,2,3,4})
   return gestion_busqueda

def menu_usuarios():

   opcion=int(input(" 1. Añadir usuario\n 2. Eliminar usuario\n 3. Buscar usuarios\n 4. Volver al menu anteriror\nQue desea hacer: "))
   gestion_usuario=validar_opcion(opcion,{1,2,3,4})
   return gestion_usuario

def menu_prestamos():
   opcion=int(input(" 1. Añadir usuario\n 2. Eliminar usuario\n 3. Buscar usuarios\n 4. Volver al menu anteriror\nQue desea hacer: "))
   gestion_prestamos=validar_opcion(opcion,{1,2,3,4})
   return gestion_prestamos




        