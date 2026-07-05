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
    ids=sorted(id for id in inventario)

    if not ids:
        new_id=1
    
    new_id=ids[-1]+1
    
    return new_id
    


        

    
    



    