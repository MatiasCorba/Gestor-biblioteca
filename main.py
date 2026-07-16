import libros,usuarios,prestamos,menus,persistencia

inventario=persistencia.cargar_inventario()
registro_usuarios=persistencia.cargar_registro_usuarios()

while True:
    gestion=menus.menu_principal()
    
    if gestion==1:
        
        while True:
            gestion_libro=menus.menu_libros()
            if gestion_libro==1:
                nombre=input("Ingrese el nombre del libro: ")
                autor=input("Ingrese nombre del autor del libro: ")
                año=input("Ingrese año de publicacion del libro: ")
                genero=input("Ingrese el genero del libro: ")
                inventario=libros.agregar_inventario(libro=nombre,autor=autor,año=año,genero=genero,inventario=inventario)
                   
            elif gestion_libro==2:
                libro=input("Ingrese el nombre del libro que desea borrar: ")
                libros.eliminar_libro(libro=libro,inventario=inventario)
                                   
            elif gestion_libro==3:

                while True:
                    gestion_busqueda=menus.menu_busqueda()

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

                        autor=None
                        año=None
                        genero=None
                        while True:
                                        
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
                                            
                            filtro=menus.menu_filtros()

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
                                print("Filtro de autor eliminado")

                            elif filtro==5:
                                if not año:
                                    print("No hay filtro de año de publicación determinado")
                                    continue
                                                
                                año=None
                                print("Filtro de año de publicacion eliminado")

                            elif filtro==6:
                                if not genero:
                                    print("No hay filtro de genero determinado")
                                    continue
                                                
                                genero=None
                                print("Filtro de genero eliminado")

                            elif filtro==7:
                                break

                            elif filtro==8:
                                break
                                            
                        if filtro==7:
                            libros.buscar_por_atributo(inventario=inventario,año=año,autor=autor,genero=genero)
                            
                    elif gestion_busqueda==5:
                                    break

            elif gestion_libro==4:
                break
                           
    elif gestion==2:

        while True:
            gestion_usuario=menus.menu_usuarios()
                   
            if gestion_usuario==1:
                nombre=input("Ingrese nombre del usuario: ")
                apellido=input("Ingrese apellido del usuario: ")
                dni=input("Ingrese dni del usuario: ")
                registro_usuarios=usuarios.registrar_usuario(nombre=nombre,apellido=apellido,dni=dni,registro_usuarios=registro_usuarios)
                   
            elif gestion_usuario==2:
                dni=input("Ingrese dni del usuario: ")
                usuarios.eliminar_usuario(dni=dni,registro_usuarios=registro_usuarios)
                                   
            elif gestion_usuario==3:
                usuarios.listar_usuarios(inventario=inventario,registro_usuarios=registro_usuarios)

            elif gestion_usuario==4:
                break
            
    elif gestion==3:
            
        while True:
            gestion_prestamo=menus.menu_prestamos()

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

    elif gestion==4:
        print("Hasta pronto!")
        break

persistencia.guardar_inventario(inventario)
persistencia.guardar_registro_usuarios(registro_usuarios)




                       
                       


