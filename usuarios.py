def registrar_usuario(nombre,apellido,dni,registro_usuarios):    
    registro_usuarios[dni]={"nombre":nombre,
                        "apellido":apellido,
                        "prestados":[]}
    
    return registro_usuarios

def buscar_usuario(dni,registro_usuarios):
    
    if dni in registro_usuarios:
        return registro_usuarios[dni]
    
    print("El dni no se encuentra registrado dentro de nuestros usuarios")
    return None






    

