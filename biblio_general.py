import libros,usuarios,prestamos

inventario={}
registro_usuarios={}

accion=1
while accion > 0 and accion < 5:
    accion=int(input("Que desea hacer:\n 1. Añadir libro\n 2. Añadir usuario\n 3. Gestionar prestamos\n 4. Finalizar gestion"))
    try:
        if accion==1:
           nombre=input("Ingrese el nombre del libro: ")
           autor=input("ingrese nombre del autor del libro: ")
           año=input("Ingrese año de publicacion del libro: ")
           genero=input("Ingrese el genero del libro: ")
           inventario=libros.agregar_inventario(nombre=nombre,autor=autor,año=año,genero=genero,inventario=inventario)
        
        elif accion==2:
            nombre=input("Ingrese su nombre: ")
            apellido=input("Ingrese su apellido: ")
            dni=input("Ingrese su dni: ")
            registro_usuarios=usuarios.agregar_usuarios(nombre=nombre,apellido=apellido,dni=dni,registro_usuarios=registro_usuarios)
        
        elif accion==3:
            gestion=1
            while gestion > 0 and gestion < 4:
                gestion=int(input("Que desea hacer:\n 1. Prestar libro\n 2. Devolver libro\n 3. Volver al menu anterior"))
                try:
                    if gestion==1:
                        libro=input("Indique el nombre del libro a prestar: ")
                        dni=int(input("Indique DNI del usuario: "))
                        prestamos.prestar_libro(dni=dni,libro=libro,registro_usuarios=registro_usuarios,inventario=inventario)
                        
                    elif gestion==2:
                        libro=input("Indique el nombre del libro a devolver: ")
                        dni=int(input("Indique DNI del usuario: "))
                        prestamos.prestar_libro(dni=dni,libro=libro,registro_usuarios=registro_usuarios,inventario=inventario)

                    elif gestion==3:
                        break

                except ValueError:
                    print("Por favor seleccione el numero de la accion que desea realizar")

        elif accion==4:
            print("Hasta pronto!")
            break

    except ValueError:
        print("Por favor seleccione el numero de la accion que desea realizar")




                       
                       


