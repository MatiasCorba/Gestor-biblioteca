import json
from pathlib import Path

def cargar_inventario():
    filename="datos/inventario.json"
    if Path(filename).exists():
        with open(filename) as f_obj:
            inventario_str=json.load(f_obj)
        inventario={}
        for clave,valor in inventario_str.items():
            inventario[int(clave)]=valor
        return inventario
    
    inventario={}
    return inventario

def cargar_registro_usuarios():
    filename="datos/registro_usuarios.json"
    if Path(filename).exists():
        with open(filename) as f_obj:
            registro_usuarios=json.load(f_obj)
        return registro_usuarios
    
    registro_usuarios={}
    return registro_usuarios

def guardar_inventario(inventario):
    filename="datos/inventario.json"
    with open(filename,"w+") as f_obj:
        json.dump(inventario,f_obj)
    return

def guardar_registro_usuarios(registro_usuarios):
    filename="datos/registro_usuarios.json"
    with open(filename,"w+") as f_obj:
        json.dump(registro_usuarios,f_obj)
    return



