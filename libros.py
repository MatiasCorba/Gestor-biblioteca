def agregar_inventario(libro,autor,año,genero,inventario):
    id=generar_id(inventario)
    
    inventario[id]={"titulo":libro,
                       "autor":autor,
                       "año":año,
                       "genero":genero,
                       "disponibilidad":True}
    
    return inventario

def buscar_libro(libro,inventario):
    for id,info_libro in inventario.items():
        if info_libro["titulo"]==libro:
            return id
        
    
    print("No existe ese libro en el inventario")
    return None
    

def generar_id(inventario):
    if inventario:
       new_id=max(inventario)+1
    else:
       new_id=1
    
    return new_id
    
def listar_libros(inventario):
    if not inventario:
        print("No hay libros registrados")
        return
    print("Nuestros libros:")
    for id,libro in inventario.items():
        print(f"ID={id}\nLibro:{libro["titulo"]}\nAutor:{libro["autor"]}\nAño de publicacion:{libro["año"]}\nGenero:{libro["genero"]}")
        print("-------------------------")
    return
    

def eliminar_libro(libro,inventario):
    busqueda=buscar_libro(libro=libro,inventario=inventario)
    if busqueda:
        if inventario[busqueda]["disponibilidad"]:
            inventario.pop(busqueda)
            print(f"El libro {libro} ha sido borrado del inventario.")
            return
        print("El libro no puede ser eliminado del inventario porque ha sido prestado a un usuario")
        return
    
    return

    

        

    
    



    