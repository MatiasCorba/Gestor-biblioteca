def agregar_inventario(libro,autor,año,genero,inventario):
    id=generar_id(inventario)
    libro=libro.lower()
    autor=autor.lower()
    genero=genero.lower()
    
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

def eliminar_libro(libro,inventario):
    libro=libro.lower()
    busqueda=buscar_libro(libro=libro,inventario=inventario)
    
    if busqueda:
        if inventario[busqueda]["disponibilidad"]:
            inventario.pop(busqueda)
            print(f"El libro {libro} ha sido borrado del inventario.")
            return
        print("El libro no puede ser eliminado del inventario porque ha sido prestado a un usuario")
        return
    
    return

def buscar_por_atributo(inventario, autor=None, año=None, genero=None, disponibilidad=None):
    if not inventario:
        print("No hay libros registrados")
        return
    
    libros=[]
    for id,info_libro in inventario.items():
        if disponibilidad==True:
            if info_libro["disponibilidad"]!=disponibilidad:
                continue
        if disponibilidad==False:
            if info_libro["disponibilidad"]!=disponibilidad:
                continue
        if autor:
            if info_libro["autor"]!=autor:
                continue
        if año:
            if info_libro["año"]!=año:
                continue
        if genero:
            if info_libro["genero"]!=genero:
                continue
        libros.append((id,info_libro))
    
    if not libros:
        print("No se encontaron resultados para su busqueda")
        return

    for id,libro in libros:       
        print(f"ID={id}\nLibro:{libro["titulo"]}\nAutor:{libro["autor"]}\nAño de publicacion:{libro["año"]}\nGenero:{libro["genero"]}")
        print("-------------------------")
    return



        
        
            

    

        

    
    



    