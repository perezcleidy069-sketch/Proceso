from docs import carga_datos, guarda_datos, almacenes
import funcionalidad as funcion

ARCHIVO="almacen.json"

def iniciar_programa():
   carga_datos(ARCHIVO)

while True:
    funcion.separador()
    print(f"---GESTION DE ALMACEN ({len(almacenes)}item)---")
    funcion.separador()
    menu="""
    1. Añadir Elementos
    2. Ver todos los elementos
    3. Buscar elementos
    4. Editar elementos
    5. Eliminar elementos
    6. Ver todas las categorias
    7. Guardar y Cargar elementos
    8. Salir"""
    print(menu)

    opc=funcion.pedir_opcion()

    if opc == 1:
        funcion.añadir_elemento()
    elif opc==2:
        funcion.ver_todos_elementos()
    elif opc==3: 
        funcion.buscar_elemento()
    elif opc==4:
        funcion.editar_elementos()
    elif opc==5:
        funcion.eliminar_elemento()
    elif opc==6:
        funcion.ver_todas_categorias()
    elif opc==7:
        print(carga_datos, guarda_datos)
    
    else: 
        print("Gracias por utilizar nuestro sitio")

if__name=="__main__"
iniciar_programa()