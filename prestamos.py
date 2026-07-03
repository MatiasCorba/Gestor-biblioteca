def prestar_libro(registro_usuarios,dni,inventario,libro):
    if libro in inventario:
        if inventario[libro]["disponibilidad"]:
            registro_usuarios[dni]["prestados"].append(inventario[libro]["nombre"])
            inventario[libro]["disponibilidad"]=False
            print("Libro prestado")
            return
        else:
            print("Este libro ya fue prestado")
            return
    print("No existe ese libro en el inventario")

def devolver_libro(registro_usuarios,dni,inventario,libro):
    registro_usuarios[dni]["prestados"].pop(inventario[libro]["nombre"])
    inventario[libro]["disponibilidad"]=True
    print("Libro devuelto")
    return
    