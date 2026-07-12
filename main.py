import libros,usuarios,prestamos

inventario={}
registro_usuarios={}

gestion=1
while gestion > 0 and gestion < 5:
    try:
        gestion=int(input(" 1. Gestionar libros\n 2. Gestionar usuarios\n 3. Gestionar prestamos\n 4. Finalizar gestion\nQue desea hacer: "))
        if gestion==1:
           
           gestion_libro=1
           while gestion_libro > 0 and gestion_libro < 5:
               try:
                   gestion_libro=int(input(" 1. Añadir libro\n 2. Eliminar libro\n 3. Buscar libros\n 4. Volver al menu anteriror\nQue desea hacer: "))
                   
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

                        gestion_busqueda=1
                        while gestion_busqueda > 0 and gestion_busqueda < 6:
                            try:
                                gestion_busqueda=int(input(" 1. Listar todos\n 2. Listar disponibles para prestar\n 3. Listar prestados\n 4. Buscar por filtro\n 5. Volver al menu anterior\nQue desea hacer:"))

                                if gestion_busqueda==1:
                                    print("Nuestros libros:")
                                    libros.buscar_por_atributo(inventario=inventario)

                                elif gestion_busqueda==2:
                                    print("Libros disponibles:")
                                    libros.buscar_por_atributo(inventario=inventario, disponibilidad=True)

                                elif gestion_busqueda==3:
                                    print("Libros prestados:")
                                    libros.buscar_por_atributo(inventario=inventario, disponibilidad=False)

                                elif gestion_busqueda==4:

                                    filtro=1
                                    autor=None
                                    año=None
                                    genero=None
                                    while filtro > 0 and filtro < 9:
                                        
                                        print("Filtros:")
                                        if not autor:
                                            print("Autor: Ninguno")
                                        else:
                                            print("Autor:",autor)
                                        if not año:
                                            print("Año: Ninguno")
                                        else:
                                            print("Año:",año)
                                        if not genero:
                                            print("Genero: Ninguno")
                                        else:
                                            print("Genero:",genero)    
                                            
                                        try:
                                            filtro=int(input(" 1. Autor\n 2. Año de publicacion\n 3. Genero\n 4.Quitar filtro de autor\n 5. Quitar filtro de año\n 6.Quitar filtro de genero\n 7. Buscar\n 8. Volver\nDetermine filtro de la busqueda: "))

                                            if filtro==1:
                                                autor=input("Nombre del autor: ")
                                                autor=autor.lower()
                                            
                                            elif filtro==2:
                                                año=input("Año de publicacion: ")

                                            elif filtro==3:
                                                genero=input("Genero: ")
                                                genero=genero.lower()
                                            
                                            elif filtro==4:
                                                if not autor:
                                                    print("No hay filtro de autor determinado")
                                                    continue
                                                
                                                autor=None
                                                print("Filtro eliminado")

                                            elif filtro==5:
                                                if not año:
                                                    print("No hay filtro de año de publicación determinado")
                                                    continue
                                                
                                                año=None
                                                print("Filtro eliminado")

                                            elif filtro==6:
                                                if not genero:
                                                    print("No hay filtro de genero determinado")
                                                    continue
                                                
                                                genero=None
                                                print("Filtro eliminado")

                                            elif filtro==7:
                                               break

                                            elif filtro==8:
                                                break
                                            
                                        except ValueError:
                                            print("Por favor seleccione el numero de la accion que desea realizar")
                                    if filtro==7:
                                        libros.buscar_por_atributo(inventario=inventario,año=año,autor=autor,genero=genero)
                            
                                elif gestion_busqueda==5:
                                    break

                            except ValueError:
                                print("Por favor seleccione el numero de la accion que desea realizar")

                   elif gestion_libro==4:
                       break
               
               except ValueError:
                   print("Por favor seleccione el numero de la accion que desea realizar")
                   
        elif gestion==2:

            gestion_usuario=1
            while gestion_usuario > 0 and gestion_usuario < 5:
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
            
        elif gestion==3:
            
            gestion_prestamo=1
            while gestion_prestamo > 0 and gestion_prestamo < 4:
                try:
                    gestion_prestamo=int(input(" 1. Prestar libro\n 2. Devolver libro\n 3. Volver al menu anterior\nQue desea hacer: "))
                    if gestion_prestamo==1:
                        libro=input("Indique el nombre del libro a prestar: ")
                        dni=input("Indique DNI del usuario: ")
                        prestamos.prestar_libro(dni=dni,libro=libro,registro_usuarios=registro_usuarios,inventario=inventario)
                        
                    elif gestion_prestamo==2:
                        libro=input("Indique el nombre del libro a devolver: ")
                        dni=input("Indique DNI del usuario: ")
                        prestamos.devolver_libro(dni=dni,libro=libro,registro_usuarios=registro_usuarios,inventario=inventario)

                    elif gestion_prestamo==3:
                        break

                except ValueError:
                    print("Por favor seleccione el numero de la accion que desea realizar")

        elif gestion==4:
            print("Hasta pronto!")
            break

    except ValueError:
        print("Por favor seleccione el numero de la accion que desea realizar")




                       
                       


