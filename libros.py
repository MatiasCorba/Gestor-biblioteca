def agregar_inventario(libro,autor,año,genero,inventario):
    inventario[libro]={"titulo":libro,
                       "autor":autor,
                       "año":año,
                       "genero":genero,
                       "disponibilidad":True}
    
    return inventario

def buscar_libro(libro,inventario):
    
    if libro in inventario:
        return True
    
    return False
    

    


        

    
    



    