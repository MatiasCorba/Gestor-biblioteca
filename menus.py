def validar_opcion(menu,opciones):
    while True:
        try:
            opcion=int(input(menu))  
            if opcion in opciones:
               return opcion
      
            print("Por favor seleccione el numero de la accion que desea realizar")
        except ValueError:
            print("Por favor seleccione el numero de la accion que desea realizar")

def menu_principal():
   menu=" 1. Gestionar libros\n 2. Gestionar usuarios\n 3. Gestionar prestamos\n 4. Finalizar gestion\nQue desea hacer: "
   gestion=validar_opcion(menu,{1,2,3,4})
   return gestion  

def menu_libros():
   menu=" 1. Añadir libro\n 2. Eliminar libro\n 3. Buscar libros\n 4. Volver al menu anteriror\nQue desea hacer: "
   gestion_libro=validar_opcion(menu,{1,2,3,4})
   return gestion_libro

def menu_filtros():
   menu=" 1. Autor\n 2. Año de publicacion\n 3. Genero\n 4.Quitar filtro de autor\n 5. Quitar filtro de año\n 6.Quitar filtro de genero\n 7. Buscar\n 8. Volver\nDetermine filtro de la busqueda: "
   gestion_filtro=validar_opcion(menu,{1,2,3,4,5,6,7,8})
   return gestion_filtro

def menu_busqueda():
   menu=" 1. Listar todos\n 2. Listar disponibles para prestar\n 3. Listar prestados\n 4. Buscar por filtro\n 5. Volver al menu anterior\nQue desea hacer:"
   gestion_busqueda=validar_opcion(menu,{1,2,3,4,5})
   return gestion_busqueda

def menu_usuarios():
   menu=" 1. Añadir usuario\n 2. Eliminar usuario\n 3. Listar usuarios\n 4. Volver al menu anteriror\nQue desea hacer: "
   gestion_usuario=validar_opcion(menu,{1,2,3,4})
   return gestion_usuario

def menu_prestamos():
   menu=" 1. Prestar libro\n 2. Devolver libro\n 3. Volver al menu anterior\nQue desea hacer: "
   gestion_prestamos=validar_opcion(menu,{1,2,3})
   return gestion_prestamos




        