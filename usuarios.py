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

def listar_usuarios(registro_usuarios,inventario):
    if registro_usuarios:
       print("Usuarios registrados:")
       for dni,usuario in registro_usuarios.items():
           print(f"Nombre:{usuario["nombre"]}\nApellido:{usuario["apellido"]}\nDNI:{dni}")
           if usuario["prestados"]:
               print("Libros prestados:")
               for id in usuario["prestados"]:
                   print(inventario[id]["titulo"])
           else:
               print("No tiene libros prestados")
       return
    print("No hay usuarios registrados")
    return

def eliminar_usuario(dni,registro_usuarios):
    if dni in registro_usuarios:
        if not registro_usuarios[dni]["prestados"]:
           registro_usuarios.pop(dni)
           print("El usuario ha sido eliminado del registro")
           return
        print("El usuario no puede ser eliminado porque aun cuenta con libros prestados")
    
    print(f"El dni {dni} no se encuentra registrado como usuario")
    return


               







    

