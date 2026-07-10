import libros,usuarios,prestamos

inventario={}
registro_usuarios={}

accion=1
while accion > 0 and accion < 5:
    try:
        accion=int(input(" 1. Gestionar libros\n 2. Gestionar usuarios\n 3. Gestionar prestamos\n 4. Finalizar gestion\nQue desea hacer: "))
        if accion==1:
           
           gestion_libro=1
           while gestion_libro > 0 and accion < 5:
               try:
                   gestion_libro=int(input(" 1. Añadir libro\n 2. Eliminar libro\n 3. Listar libros\n 4. Volver al menu anteriror\nQue desea hacer: "))
                   
                   if gestion_libro==1:
                       nombre=input("Ingrese el nombre del libro: ")
                       autor=input("ingrese nombre del autor del libro: ")
                       año=input("Ingrese año de publicacion del libro: ")
                       genero=input("Ingrese el genero del libro: ")
                       inventario=libros.agregar_inventario(libro=nombre,autor=autor,año=año,genero=genero,inventario=inventario)
                   
                   elif gestion_libro==2:
                       libro=input("Ingrese el nombre del libro que desea borrar: ")
                       libros.eliminar_libro(libro=libro,inventario=inventario)
                                   
                   elif gestion_libro==3:
                        libros.listar_libros(inventario)

                   elif gestion_libro==4:
                       break
               
               except ValueError:
                   print("Por favor seleccione el numero de la accion que desea realizar")
                   
        elif accion==2:

            gestion_usuario=1
            while gestion_usuario > 0 and accion < 5:
               try:
                   gestion_usuario=int(input(" 1. Añadir usuario\n 2. Eliminar usuario\n 3. Listar usuarios\n 4. Volver al menu anteriror\nQue desea hacer: "))
                   
                   if gestion_usuario==1:
                       nombre=input("Ingrese su nombre: ")
                       apellido=input("Ingrese su apellido: ")
                       dni=input("Ingrese su dni: ")
                       registro_usuarios=usuarios.registrar_usuario(nombre=nombre,apellido=apellido,dni=dni,registro_usuarios=registro_usuarios)
                   
                   elif gestion_usuario==2:
                       dni=input("Ingrese el dni del usuario: ")
                       usuarios.eliminar_usuario(dni=dni,registro_usuarios=registro_usuarios)
                                   
                   elif gestion_usuario==3:
                        usuarios.listar_usuarios(inventario=inventario,registro_usuarios=registro_usuarios)

                   elif gestion_usuario==4:
                       break
               
               except ValueError:
                   print("Por favor seleccione el numero de la accion que desea realizar")
            
        elif accion==3:
            
            gestion=1
            while gestion > 0 and gestion < 4:
                try:
                    gestion=int(input(" 1. Prestar libro\n 2. Devolver libro\n 3. Volver al menu anterior\nQue desea hacer: "))
                    if gestion==1:
                        libro=input("Indique el nombre del libro a prestar: ")
                        dni=input("Indique DNI del usuario: ")
                        prestamos.prestar_libro(dni=dni,libro=libro,registro_usuarios=registro_usuarios,inventario=inventario)
                        
                    elif gestion==2:
                        libro=input("Indique el nombre del libro a devolver: ")
                        dni=input("Indique DNI del usuario: ")
                        prestamos.devolver_libro(dni=dni,libro=libro,registro_usuarios=registro_usuarios,inventario=inventario)

                    elif gestion==3:
                        break

                except ValueError:
                    print("Por favor seleccione el numero de la accion que desea realizar")

        elif accion==4:
            print("Hasta pronto!")
            break

    except ValueError:
        print("Por favor seleccione el numero de la accion que desea realizar")




                       
                       


