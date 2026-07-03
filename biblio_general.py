import libros,usuarios,prestamos

accion=1
while accion > 0 and accion < 4:
    accion=int(input("Que desea hacer:\n 1. Añadir libro\n 2. Añadir usuario\n 3. Gestionar prestamos"))
    try:
        if accion==1:
           nombre=input("Ingrese el nombre del libro: ")
           autor=input("ingrese nombre del autor del libro: ")
           año=input("Ingrese año de publicacion del libro: ")
           genero=input("Ingrese el genero del libro: ")
           inventario=libros.agregar_inventario(nombre=nombre,autor=autor,año=año,genero=genero)
        
        if accion==2:
            nombre=input("Ingrese su nombre: ")
            apellido=input("Ingrese su apellido: ")
            dni=input("Ingrese su dni: ")
            registro=usuarios.agregar_usuarios(nombre=nombre,apellido=apellido,dni=dni)

                       
                       


