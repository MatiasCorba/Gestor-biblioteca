import libros, usuarios


def prestar_libro(registro_usuarios,dni,inventario,libro):
    busqueda=libros.buscar_libro(inventario=inventario,libro=libro)
    usuario=usuarios.buscar_usuario(dni=dni,registro_usuarios=registro_usuarios)

    if busqueda and usuario:
        if inventario[busqueda]["disponibilidad"]:
            usuario["prestados"].append(busqueda)
            inventario[busqueda]["disponibilidad"]=False
            print("Libro prestado.")
            return
        
        print("Este libro ya fue prestado.")
        return
    
    return
    


def devolver_libro(registro_usuarios,dni,inventario,libro):
    busqueda=libros.buscar_libro(inventario=inventario,libro=libro)
    usuario=usuarios.buscar_usuario(dni=dni,registro_usuarios=registro_usuarios)

    
    if busqueda and usuario:
        if busqueda in usuario["prestados"]:
           usuario["prestados"].remove(busqueda)
           inventario[busqueda]["disponibilidad"]=True
           print("Libro devuelto.")
           return
        else:
            print("El libro no ha sido prestado al usuario indicado.")
    return
    